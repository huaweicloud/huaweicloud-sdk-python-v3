# coding: utf-8

import pprint
import re

import six





class ListSpecialThrottlingConfigurationsV2Request:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'throttle_id': 'str',
        'object_type': 'str',
        'app_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'throttle_id': 'throttle_id',
        'object_type': 'object_type',
        'app_name': 'app_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, throttle_id=None, object_type=None, app_name=None, offset=None, limit=None):
        """ListSpecialThrottlingConfigurationsV2Request - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._throttle_id = None
        self._object_type = None
        self._app_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        self.throttle_id = throttle_id
        if object_type is not None:
            self.object_type = object_type
        if app_name is not None:
            self.app_name = app_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        """Gets the instance_id of this ListSpecialThrottlingConfigurationsV2Request.

        实例编号

        :return: The instance_id of this ListSpecialThrottlingConfigurationsV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListSpecialThrottlingConfigurationsV2Request.

        实例编号

        :param instance_id: The instance_id of this ListSpecialThrottlingConfigurationsV2Request.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def throttle_id(self):
        """Gets the throttle_id of this ListSpecialThrottlingConfigurationsV2Request.

        流控策略的ID

        :return: The throttle_id of this ListSpecialThrottlingConfigurationsV2Request.
        :rtype: str
        """
        return self._throttle_id

    @throttle_id.setter
    def throttle_id(self, throttle_id):
        """Sets the throttle_id of this ListSpecialThrottlingConfigurationsV2Request.

        流控策略的ID

        :param throttle_id: The throttle_id of this ListSpecialThrottlingConfigurationsV2Request.
        :type: str
        """
        self._throttle_id = throttle_id

    @property
    def object_type(self):
        """Gets the object_type of this ListSpecialThrottlingConfigurationsV2Request.

        特殊流控类型：APP, USER

        :return: The object_type of this ListSpecialThrottlingConfigurationsV2Request.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this ListSpecialThrottlingConfigurationsV2Request.

        特殊流控类型：APP, USER

        :param object_type: The object_type of this ListSpecialThrottlingConfigurationsV2Request.
        :type: str
        """
        self._object_type = object_type

    @property
    def app_name(self):
        """Gets the app_name of this ListSpecialThrottlingConfigurationsV2Request.

        筛选的特殊应用名称

        :return: The app_name of this ListSpecialThrottlingConfigurationsV2Request.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ListSpecialThrottlingConfigurationsV2Request.

        筛选的特殊应用名称

        :param app_name: The app_name of this ListSpecialThrottlingConfigurationsV2Request.
        :type: str
        """
        self._app_name = app_name

    @property
    def offset(self):
        """Gets the offset of this ListSpecialThrottlingConfigurationsV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListSpecialThrottlingConfigurationsV2Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSpecialThrottlingConfigurationsV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListSpecialThrottlingConfigurationsV2Request.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSpecialThrottlingConfigurationsV2Request.

        每页显示的条目数量

        :return: The limit of this ListSpecialThrottlingConfigurationsV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSpecialThrottlingConfigurationsV2Request.

        每页显示的条目数量

        :param limit: The limit of this ListSpecialThrottlingConfigurationsV2Request.
        :type: int
        """
        self._limit = limit

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
        if not isinstance(other, ListSpecialThrottlingConfigurationsV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
