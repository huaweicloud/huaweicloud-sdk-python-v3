# coding: utf-8

import pprint
import re

import six





class DeleteResourceRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_request_id': 'str',
        'accept_language': 'str',
        'corp_id': 'str',
        'force_edit_flag': 'bool',
        'body': 'list[str]'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'accept_language': 'Accept-Language',
        'corp_id': 'corp_id',
        'force_edit_flag': 'forceEditFlag',
        'body': 'body'
    }

    def __init__(self, x_request_id=None, accept_language=None, corp_id=None, force_edit_flag=False, body=None):
        """DeleteResourceRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_request_id = None
        self._accept_language = None
        self._corp_id = None
        self._force_edit_flag = None
        self._body = None
        self.discriminator = None

        if x_request_id is not None:
            self.x_request_id = x_request_id
        if accept_language is not None:
            self.accept_language = accept_language
        self.corp_id = corp_id
        if force_edit_flag is not None:
            self.force_edit_flag = force_edit_flag
        if body is not None:
            self.body = body

    @property
    def x_request_id(self):
        """Gets the x_request_id of this DeleteResourceRequest.


        :return: The x_request_id of this DeleteResourceRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this DeleteResourceRequest.


        :param x_request_id: The x_request_id of this DeleteResourceRequest.
        :type: str
        """
        self._x_request_id = x_request_id

    @property
    def accept_language(self):
        """Gets the accept_language of this DeleteResourceRequest.


        :return: The accept_language of this DeleteResourceRequest.
        :rtype: str
        """
        return self._accept_language

    @accept_language.setter
    def accept_language(self, accept_language):
        """Sets the accept_language of this DeleteResourceRequest.


        :param accept_language: The accept_language of this DeleteResourceRequest.
        :type: str
        """
        self._accept_language = accept_language

    @property
    def corp_id(self):
        """Gets the corp_id of this DeleteResourceRequest.


        :return: The corp_id of this DeleteResourceRequest.
        :rtype: str
        """
        return self._corp_id

    @corp_id.setter
    def corp_id(self, corp_id):
        """Sets the corp_id of this DeleteResourceRequest.


        :param corp_id: The corp_id of this DeleteResourceRequest.
        :type: str
        """
        self._corp_id = corp_id

    @property
    def force_edit_flag(self):
        """Gets the force_edit_flag of this DeleteResourceRequest.


        :return: The force_edit_flag of this DeleteResourceRequest.
        :rtype: bool
        """
        return self._force_edit_flag

    @force_edit_flag.setter
    def force_edit_flag(self, force_edit_flag):
        """Sets the force_edit_flag of this DeleteResourceRequest.


        :param force_edit_flag: The force_edit_flag of this DeleteResourceRequest.
        :type: bool
        """
        self._force_edit_flag = force_edit_flag

    @property
    def body(self):
        """Gets the body of this DeleteResourceRequest.

        待删除的资源Id列表，最多支持批量处理100个

        :return: The body of this DeleteResourceRequest.
        :rtype: list[str]
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DeleteResourceRequest.

        待删除的资源Id列表，最多支持批量处理100个

        :param body: The body of this DeleteResourceRequest.
        :type: list[str]
        """
        self._body = body

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeleteResourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
