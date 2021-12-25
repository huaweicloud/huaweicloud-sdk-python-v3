# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEdgeNodesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'limit': 'str',
        'offset': 'str',
        'device_id': 'str',
        'device_name': 'str',
        'app_name': 'str',
        'tags': 'str',
        'ief_instance_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'limit': 'limit',
        'offset': 'offset',
        'device_id': 'device_id',
        'device_name': 'device_name',
        'app_name': 'app_name',
        'tags': 'tags',
        'ief_instance_id': 'ief-instance-id'
    }

    def __init__(self, name=None, limit=None, offset=None, device_id=None, device_name=None, app_name=None, tags=None, ief_instance_id=None):
        """ListEdgeNodesRequest - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._limit = None
        self._offset = None
        self._device_id = None
        self._device_name = None
        self._app_name = None
        self._tags = None
        self._ief_instance_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if device_id is not None:
            self.device_id = device_id
        if device_name is not None:
            self.device_name = device_name
        if app_name is not None:
            self.app_name = app_name
        if tags is not None:
            self.tags = tags
        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id

    @property
    def name(self):
        """Gets the name of this ListEdgeNodesRequest.

        边缘节点名称，模糊匹配

        :return: The name of this ListEdgeNodesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListEdgeNodesRequest.

        边缘节点名称，模糊匹配

        :param name: The name of this ListEdgeNodesRequest.
        :type: str
        """
        self._name = name

    @property
    def limit(self):
        """Gets the limit of this ListEdgeNodesRequest.

        每页显示的条目数量，取值范围1~1000，默认为500

        :return: The limit of this ListEdgeNodesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEdgeNodesRequest.

        每页显示的条目数量，取值范围1~1000，默认为500

        :param limit: The limit of this ListEdgeNodesRequest.
        :type: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListEdgeNodesRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :return: The offset of this ListEdgeNodesRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEdgeNodesRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :param offset: The offset of this ListEdgeNodesRequest.
        :type: str
        """
        self._offset = offset

    @property
    def device_id(self):
        """Gets the device_id of this ListEdgeNodesRequest.

        按终端设备ID查找

        :return: The device_id of this ListEdgeNodesRequest.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ListEdgeNodesRequest.

        按终端设备ID查找

        :param device_id: The device_id of this ListEdgeNodesRequest.
        :type: str
        """
        self._device_id = device_id

    @property
    def device_name(self):
        """Gets the device_name of this ListEdgeNodesRequest.

        按绑定终端设备名称查找

        :return: The device_name of this ListEdgeNodesRequest.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this ListEdgeNodesRequest.

        按绑定终端设备名称查找

        :param device_name: The device_name of this ListEdgeNodesRequest.
        :type: str
        """
        self._device_name = device_name

    @property
    def app_name(self):
        """Gets the app_name of this ListEdgeNodesRequest.

        按应用名称查找

        :return: The app_name of this ListEdgeNodesRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ListEdgeNodesRequest.

        按应用名称查找

        :param app_name: The app_name of this ListEdgeNodesRequest.
        :type: str
        """
        self._app_name = app_name

    @property
    def tags(self):
        """Gets the tags of this ListEdgeNodesRequest.

        标签的key和value通过点连接， 多个标签通过逗号连接，如：tags=key1.value1,key2.value2

        :return: The tags of this ListEdgeNodesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListEdgeNodesRequest.

        标签的key和value通过点连接， 多个标签通过逗号连接，如：tags=key1.value1,key2.value2

        :param tags: The tags of this ListEdgeNodesRequest.
        :type: str
        """
        self._tags = tags

    @property
    def ief_instance_id(self):
        """Gets the ief_instance_id of this ListEdgeNodesRequest.

        铂金版实例ID，专业版实例为空值

        :return: The ief_instance_id of this ListEdgeNodesRequest.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        """Sets the ief_instance_id of this ListEdgeNodesRequest.

        铂金版实例ID，专业版实例为空值

        :param ief_instance_id: The ief_instance_id of this ListEdgeNodesRequest.
        :type: str
        """
        self._ief_instance_id = ief_instance_id

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
        if not isinstance(other, ListEdgeNodesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
