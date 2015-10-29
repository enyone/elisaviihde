# Elisa Viihde API Python implementation tests
# License: GPLv3
# Author: Juho Tykkala

import elisaviihde
from nose.tools import *
from httmock import urlmatch, HTTMock

# Mocks
@urlmatch(netloc=r'(.*\.)?elisaviihde\.fi$')
def elisaviihde_api_mock(url, request):
  if url.path == "/":
    return {'status_code': 200, 'content': '<html></html>'}
  elif url.path == "/api/sso/authcode":
    return {'status_code': 200, 'content': '{"code":"dummy-token"}'}
  elif url.path == "/api/user":
    return {'status_code': 200, 'content': '{"username":"dummy-user"}'}
  elif url.path == "/api/user/logout":
    return {'status_code': 200, 'content': '{}'}
  elif url.path == "/tallenteet/api/folders":
    return {'status_code': 200, 'content': '{"folders":[{"id":0,"folders":[{"id":1,"name":"dummy-folder"}]}]}'}
  elif url.path == "/tallenteet/api/folder/0":
    return {'status_code': 200, 'content': '{"recordingsCount":1}'}
  elif url.path == "/tallenteet/api/recordings/0":
    return {'status_code': 200, 'content': '[{"name":"dummy-recording"}]'}
  elif url.path == "/tallenteet/katso/0":
    return {'status_code': 200, 'content': 'data-section="recording-player" data-url="http://test.com/test"'}
  elif url.path == "/ohjelmaopas/ohjelma/1234":
    return {'status_code': 200, 'content': '\n<p itemprop="name">dummy-channel-name</p>\n'
              + '<p itemprop="description">dummy-service-description</p>\n'
              + '<span itemprop="startDate">01.02.2014 13:14</span>\n'
              + '<h3 itemprop="name" id="data-programid">dummy-service-name</h3>\n'}
  elif url.path == "/ohjelmaopas/ohjelma/1239":
    return {'status_code': 200, 'content': '\n<p itemprop="name">dummy-channel-name</p>\n'
              + '<p itemprop="description">dummy-service-description</p>\n'
              + '<span itemprop="startDate">01.02.2014a 13:14</span>\n'
              + '<h3 itemprop="name" id="data-programid">dummy-service-name</h3>\n'}
  else:
    return {'status_code': 500}

@urlmatch(netloc=r'(.*\.)?elisaviihde\.fi$')
def elisaviihde_api_mock_asshole(url, request):
  return {'status_code': 500}

@urlmatch(netloc=r'(.*\.)?elisaviihde\.fi$')
def elisaviihde_api_mock_badjson(url, request):
  return {'status_code': 200, 'content': '{"rew. ""ssdfg}  s'}

@urlmatch(netloc=r'(.*\.)?elisa\.fi$')
def elisaviihde_sso_mock(url, request):
  if url.path == "/sso/login":
    return {'status_code': 200}
  else:
    return {'status_code': 500}

@urlmatch(netloc=r'(.*\.)?elisa\.fi$')
def elisaviihde_sso_mock_asshole(url, request):
  return {'status_code': 500}

# Tests
def test_elisa_init_ok():
  with HTTMock(elisaviihde_api_mock):
    elisa = elisaviihde.elisaviihde(False)
  assert elisa.islogged() == False

@raises(Exception)
def test_elisa_init_fail():
  with HTTMock(elisaviihde_api_mock_asshole):
    elisa = elisaviihde.elisaviihde(False)

def test_elisa_login_ok():
  with HTTMock(elisaviihde_api_mock, elisaviihde_sso_mock):
    elisa = elisaviihde.elisaviihde(False)
    elisa.login("foo", "bar")
    assert elisa.islogged() == True
  assert elisa.gettoken() == "dummy-token"

@raises(Exception)
def test_elisa_login_fail():
  with HTTMock(elisaviihde_api_mock, elisaviihde_sso_mock_asshole):
    elisa = elisaviihde.elisaviihde(False)
    elisa.login("foo", "bar")

@raises(Exception)
def test_elisa_login_fail2():
  with HTTMock(elisaviihde_api_mock_badjson, elisaviihde_sso_mock):
    elisa = elisaviihde.elisaviihde(False)
    elisa.login("foo", "bar")

def test_elisa_logout_ok():
  with HTTMock(elisaviihde_api_mock, elisaviihde_sso_mock):
    elisa = elisaviihde.elisaviihde(False)
    elisa.login("foo", "bar")
    elisa.close()
  assert elisa.gettoken() == None

def test_elisa_user():
  with HTTMock(elisaviihde_api_mock, elisaviihde_sso_mock):
    elisa = elisaviihde.elisaviihde(False)
    elisa.login("foo", "bar")
    user = elisa.getuser()
  assert user["username"] == "dummy-user"

def test_elisa_sessions():
  with HTTMock(elisaviihde_api_mock, elisaviihde_sso_mock):
    elisa = elisaviihde.elisaviihde(False)
    elisa.login("foo", "bar")
    elisa.setsession({"foo":"123"})
    assert elisa.getsession() == {"foo":"123"}

def test_elisa_folders():
  with HTTMock(elisaviihde_api_mock, elisaviihde_sso_mock):
    elisa = elisaviihde.elisaviihde(False)
    elisa.login("foo", "bar")
    folders = elisa.getfolders()
  assert folders[0]["name"] == "dummy-folder"

def test_elisa_recordings():
  with HTTMock(elisaviihde_api_mock, elisaviihde_sso_mock):
    elisa = elisaviihde.elisaviihde(False)
    elisa.login("foo", "bar")
    recordings = elisa.getrecordings(0)
  assert recordings[0]["name"] == "dummy-recording"

def test_elisa_program():
  with HTTMock(elisaviihde_api_mock, elisaviihde_sso_mock):
    elisa = elisaviihde.elisaviihde(False)
    elisa.login("foo", "bar")
    program = elisa.getprogram(1234)
  assert program["serviceName"] == "dummy-channel-name"
  assert program["name"] == "dummy-service-name"
  assert program["startTimeUTC"] > 1300000000000
  assert program["description"] == "dummy-service-description"

def test_elisa_program_fail():
  with HTTMock(elisaviihde_api_mock, elisaviihde_sso_mock):
    elisa = elisaviihde.elisaviihde(False)
    elisa.login("foo", "bar")
    program = elisa.getprogram(1239)
  assert program["serviceName"] == "dummy-channel-name"
  assert program["description"] == "dummy-service-description"

def test_elisa_streamuri():
  with HTTMock(elisaviihde_api_mock, elisaviihde_sso_mock):
    elisa = elisaviihde.elisaviihde(False)
    elisa.login("foo", "bar")
    streamuri = elisa.getstreamuri(0)
  assert streamuri == "http://test.com/test"

