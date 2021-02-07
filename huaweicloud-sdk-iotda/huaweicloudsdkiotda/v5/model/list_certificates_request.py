# coding: utf-8

import pprint
import re

import six





class ListCertificatesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []
    sensitive_list.append('sp_auth_token')
    sensitive_list.append('stage_auth_token')

    openapi_types = {
        'sp_auth_token': 'str',
        'stage_auth_token': 'str',
        'instance_id': 'str',
        'app_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'sp_auth_token': 'Sp-Auth-Token',
        'stage_auth_token': 'Stage-Auth-Token',
        'instance_id': 'Instance-Id',
        'app_id': 'app_id',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset'
    }

    def __init__(self, sp_auth_token=None, stage_auth_token=None, instance_id=None, app_id=None, limit=10, marker='ffffffffffffffffffffffff', offset=0):
        """ListCertificatesRequest - a model defined in huaweicloud sdk"""
        
        

        self._sp_auth_token = None
        self._stage_auth_token = None
        self._instance_id = None
        self._app_id = None
        self._limit = None
        self._marker = None
        self._offset = None
        self.discriminator = None

        if sp_auth_token is not None:
            self.sp_auth_token = sp_auth_token
        if stage_auth_token is not None:
            self.stage_auth_token = stage_auth_token
        if instance_id is not None:
            self.instance_id = instance_id
        if app_id is not None:
            self.app_id = app_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset

    @property
    def sp_auth_token(self):
        """Gets the sp_auth_token of this ListCertificatesRequest.


        :return: The sp_auth_token of this ListCertificatesRequest.
        :rtype: str
        """
        return self._sp_auth_token

    @sp_auth_token.setter
    def sp_auth_token(self, sp_auth_token):
        """Sets the sp_auth_token of this ListCertificatesRequest.


        :param sp_auth_token: The sp_auth_token of this ListCertificatesRequest.
        :type: str
        """
        self._sp_auth_token = sp_auth_token

    @property
    def stage_auth_token(self):
        """Gets the stage_auth_token of this ListCertificatesRequest.


        :return: The stage_auth_token of this ListCertificatesRequest.
        :rtype: str
        """
        return self._stage_auth_token

    @stage_auth_token.setter
    def stage_auth_token(self, stage_auth_token):
        """Sets the stage_auth_token of this ListCertificatesRequest.


        :param stage_auth_token: The stage_auth_token of this ListCertificatesRequest.
        :type: str
        """
        self._stage_auth_token = stage_auth_token

    @property
    def instance_id(self):
        """Gets the instance_id of this ListCertificatesRequest.


        :return: The instance_id of this ListCertificatesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListCertificatesRequest.


        :param instance_id: The instance_id of this ListCertificatesRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def app_id(self):
        """Gets the app_id of this ListCertificatesRequest.


        :return: The app_id of this ListCertificatesRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListCertificatesRequest.


        :param app_id: The app_id of this ListCertificatesRequest.
        :type: str
        """
        self._app_id = app_id

    @property
    def limit(self):
        """Gets the limit of this ListCertificatesRequest.


        :return: The limit of this ListCertificatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCertificatesRequest.


        :param limit: The limit of this ListCertificatesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListCertificatesRequest.


        :return: The marker of this ListCertificatesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListCertificatesRequest.


        :param marker: The marker of this ListCertificatesRequest.
        :type: str
        """
        self._marker = marker

    @property
    def offset(self):
        """Gets the offset of this ListCertificatesRequest.


        :return: The offset of this ListCertificatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCertificatesRequest.


        :param offset: The offset of this ListCertificatesRequest.
        :type: int
        """
        self._offset = offset

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
        if not isinstance(other, ListCertificatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
