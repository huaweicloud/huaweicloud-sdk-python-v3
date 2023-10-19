# coding: utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""

import six


class SdkException(Exception):
    def __init__(self, error_msg):
        """
        The base exception class.
        """
        super(SdkException, self).__init__()
        self.error_msg = error_msg

    def __str__(self):
        return "%s - %s" % (self.__class__.__name__, self.error_msg)


class ConnectionException(SdkException):
    def __init__(self, error_msg):
        """
        The base exception class of connection exceptions.
        """
        super(ConnectionException, self).__init__(error_msg)


class HostUnreachableException(ConnectionException):
    def __init__(self, error_msg):
        """
        Host Unreachable Exception
        """
        super(HostUnreachableException, self).__init__(error_msg)


class SslHandShakeException(ConnectionException):
    def __init__(self, error_msg):
        """
        Ssl HandShake Exception
        """
        super(SslHandShakeException, self).__init__(error_msg)


class ServiceResponseException(SdkException):
    def __init__(self, status_code, sdk_error):
        """
        The base exception class of service response exceptions.
        """
        super(ServiceResponseException, self).__init__(sdk_error.error_msg)
        self.status_code = status_code
        self.error_code = sdk_error.error_code
        self.request_id = sdk_error.request_id
        self.encoded_auth_msg = sdk_error.encoded_auth_msg

    def __str__(self):
        return "%s - {status_code:%s,request_id:%s,error_code:%s,error_msg:%s,encoded_authorization_message:%s }" % (
            self.__class__.__name__, self.status_code, self.request_id, self.error_code, self.error_msg,
            self.encoded_auth_msg)


class ClientRequestException(ServiceResponseException):
    def __init__(self, status_code, sdk_error):
        """
        Client Request Exception
        """
        super(ClientRequestException, self).__init__(status_code, sdk_error)


class ServerResponseException(ServiceResponseException):
    def __init__(self, status_code, sdk_error):
        """
        Server Response Exception
        """
        super(ServerResponseException, self).__init__(status_code, sdk_error)


class RequestTimeoutException(SdkException):
    def __init__(self, error_msg):
        """
        The base exception class of timeout exceptions.
        """
        super(RequestTimeoutException, self).__init__(error_msg)


class CallTimeoutException(RequestTimeoutException):
    def __init__(self, error_msg):
        """
        Call Timeout Exception
        """
        super(CallTimeoutException, self).__init__(error_msg)


class RetryOutageException(RequestTimeoutException):
    def __init__(self, error_msg):
        """
        Retry Outage Exception
        """
        super(RetryOutageException, self).__init__(error_msg)


class SdkError(object):
    def __init__(self, request_id=None, error_code=None, error_msg=None, encoded_auth_msg=None):
        self.error_msg = error_msg
        self.error_code = error_code
        self.request_id = request_id
        self.encoded_auth_msg = encoded_auth_msg


def render_path(path_to_item):
    """Returns a string representation of a path"""
    result = ""
    for pth in path_to_item:
        if isinstance(pth, six.integer_types):
            result += "[{0}]".format(pth)
        else:
            result += "['{0}']".format(pth)
    return result


class ApiTypeError(TypeError):
    def __init__(self, msg, path_to_item=None, valid_classes=None,
                 key_type=None):
        """ Raises an exception for TypeErrors

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list): a list of keys an indices to get to the
                                 current_item
                                 None if unset
            valid_classes (tuple): the primitive classes that current item
                                   should be an instance of
                                   None if unset
            key_type (bool): False if our value is a value in a dict
                             True if it is a key in a dict
                             False if our item is an item in a list
                             None if unset
        """
        self.path_to_item = path_to_item
        self.valid_classes = valid_classes
        self.key_type = key_type
        full_msg = msg
        if path_to_item:
            full_msg = "%s at %s" % (msg, render_path(path_to_item))
        super(ApiTypeError, self).__init__(full_msg)


class ApiValueError(ValueError):
    def __init__(self, msg, path_to_item=None):
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list) the path to the exception in the
                received_data dict. None if unset
        """

        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "%s at %s" % (msg, render_path(path_to_item))
        super(ApiValueError, self).__init__(full_msg)


class ApiKeyError(KeyError):
    def __init__(self, msg, path_to_item=None):
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "%s at %s" % (msg, render_path(path_to_item))
        super(ApiKeyError, self).__init__(full_msg)
