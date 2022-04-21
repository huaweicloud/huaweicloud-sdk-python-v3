# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppConfigsV2Request:

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
        'offset': 'int',
        'limit': 'int',
        'app_id': 'str',
        'config_name': 'str',
        'roma_app_name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'app_id': 'app_id',
        'config_name': 'config_name',
        'roma_app_name': 'roma_app_name'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, app_id=None, config_name=None, roma_app_name=None):
        """ListAppConfigsV2Request

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param app_id: 应用编号
        :type app_id: str
        :param config_name: 应用配置名称
        :type config_name: str
        :param roma_app_name: 应用名称
        :type roma_app_name: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._app_id = None
        self._config_name = None
        self._roma_app_name = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if app_id is not None:
            self.app_id = app_id
        if config_name is not None:
            self.config_name = config_name
        if roma_app_name is not None:
            self.roma_app_name = roma_app_name

    @property
    def instance_id(self):
        """Gets the instance_id of this ListAppConfigsV2Request.

        实例ID

        :return: The instance_id of this ListAppConfigsV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListAppConfigsV2Request.

        实例ID

        :param instance_id: The instance_id of this ListAppConfigsV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ListAppConfigsV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListAppConfigsV2Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAppConfigsV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListAppConfigsV2Request.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListAppConfigsV2Request.

        每页显示的条目数量

        :return: The limit of this ListAppConfigsV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAppConfigsV2Request.

        每页显示的条目数量

        :param limit: The limit of this ListAppConfigsV2Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def app_id(self):
        """Gets the app_id of this ListAppConfigsV2Request.

        应用编号

        :return: The app_id of this ListAppConfigsV2Request.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListAppConfigsV2Request.

        应用编号

        :param app_id: The app_id of this ListAppConfigsV2Request.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def config_name(self):
        """Gets the config_name of this ListAppConfigsV2Request.

        应用配置名称

        :return: The config_name of this ListAppConfigsV2Request.
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        """Sets the config_name of this ListAppConfigsV2Request.

        应用配置名称

        :param config_name: The config_name of this ListAppConfigsV2Request.
        :type config_name: str
        """
        self._config_name = config_name

    @property
    def roma_app_name(self):
        """Gets the roma_app_name of this ListAppConfigsV2Request.

        应用名称

        :return: The roma_app_name of this ListAppConfigsV2Request.
        :rtype: str
        """
        return self._roma_app_name

    @roma_app_name.setter
    def roma_app_name(self, roma_app_name):
        """Sets the roma_app_name of this ListAppConfigsV2Request.

        应用名称

        :param roma_app_name: The roma_app_name of this ListAppConfigsV2Request.
        :type roma_app_name: str
        """
        self._roma_app_name = roma_app_name

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
        if not isinstance(other, ListAppConfigsV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
