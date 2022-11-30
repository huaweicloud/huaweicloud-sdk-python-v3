# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'offset': 'int',
        'limit': 'int',
        'object_type': 'str',
        'app_name': 'str',
        'user': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'throttle_id': 'throttle_id',
        'offset': 'offset',
        'limit': 'limit',
        'object_type': 'object_type',
        'app_name': 'app_name',
        'user': 'user'
    }

    def __init__(self, instance_id=None, throttle_id=None, offset=None, limit=None, object_type=None, app_name=None, user=None):
        """ListSpecialThrottlingConfigurationsV2Request

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param throttle_id: 流控策略的编号
        :type throttle_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500
        :type limit: int
        :param object_type: 特殊流控类型：APP，USER
        :type object_type: str
        :param app_name: 筛选的特殊应用名称
        :type app_name: str
        :param user: 筛选的特殊用户名称
        :type user: str
        """
        
        

        self._instance_id = None
        self._throttle_id = None
        self._offset = None
        self._limit = None
        self._object_type = None
        self._app_name = None
        self._user = None
        self.discriminator = None

        self.instance_id = instance_id
        self.throttle_id = throttle_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if object_type is not None:
            self.object_type = object_type
        if app_name is not None:
            self.app_name = app_name
        if user is not None:
            self.user = user

    @property
    def instance_id(self):
        """Gets the instance_id of this ListSpecialThrottlingConfigurationsV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this ListSpecialThrottlingConfigurationsV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListSpecialThrottlingConfigurationsV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this ListSpecialThrottlingConfigurationsV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def throttle_id(self):
        """Gets the throttle_id of this ListSpecialThrottlingConfigurationsV2Request.

        流控策略的编号

        :return: The throttle_id of this ListSpecialThrottlingConfigurationsV2Request.
        :rtype: str
        """
        return self._throttle_id

    @throttle_id.setter
    def throttle_id(self, throttle_id):
        """Sets the throttle_id of this ListSpecialThrottlingConfigurationsV2Request.

        流控策略的编号

        :param throttle_id: The throttle_id of this ListSpecialThrottlingConfigurationsV2Request.
        :type throttle_id: str
        """
        self._throttle_id = throttle_id

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
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSpecialThrottlingConfigurationsV2Request.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :return: The limit of this ListSpecialThrottlingConfigurationsV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSpecialThrottlingConfigurationsV2Request.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :param limit: The limit of this ListSpecialThrottlingConfigurationsV2Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def object_type(self):
        """Gets the object_type of this ListSpecialThrottlingConfigurationsV2Request.

        特殊流控类型：APP，USER

        :return: The object_type of this ListSpecialThrottlingConfigurationsV2Request.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this ListSpecialThrottlingConfigurationsV2Request.

        特殊流控类型：APP，USER

        :param object_type: The object_type of this ListSpecialThrottlingConfigurationsV2Request.
        :type object_type: str
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
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def user(self):
        """Gets the user of this ListSpecialThrottlingConfigurationsV2Request.

        筛选的特殊用户名称

        :return: The user of this ListSpecialThrottlingConfigurationsV2Request.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ListSpecialThrottlingConfigurationsV2Request.

        筛选的特殊用户名称

        :param user: The user of this ListSpecialThrottlingConfigurationsV2Request.
        :type user: str
        """
        self._user = user

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSpecialThrottlingConfigurationsV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
