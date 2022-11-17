# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeIps:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'livedata': 'list[str]',
        'shubao': 'list[str]'
    }

    attribute_map = {
        'livedata': 'livedata',
        'shubao': 'shubao'
    }

    def __init__(self, livedata=None, shubao=None):
        """NodeIps

        The model defined in huaweicloud sdk

        :param livedata: 自定义后端服务livedta组件节点ip列表
        :type livedata: list[str]
        :param shubao: API网关shubao组件节点ip列表
        :type shubao: list[str]
        """
        
        

        self._livedata = None
        self._shubao = None
        self.discriminator = None

        if livedata is not None:
            self.livedata = livedata
        if shubao is not None:
            self.shubao = shubao

    @property
    def livedata(self):
        """Gets the livedata of this NodeIps.

        自定义后端服务livedta组件节点ip列表

        :return: The livedata of this NodeIps.
        :rtype: list[str]
        """
        return self._livedata

    @livedata.setter
    def livedata(self, livedata):
        """Sets the livedata of this NodeIps.

        自定义后端服务livedta组件节点ip列表

        :param livedata: The livedata of this NodeIps.
        :type livedata: list[str]
        """
        self._livedata = livedata

    @property
    def shubao(self):
        """Gets the shubao of this NodeIps.

        API网关shubao组件节点ip列表

        :return: The shubao of this NodeIps.
        :rtype: list[str]
        """
        return self._shubao

    @shubao.setter
    def shubao(self, shubao):
        """Sets the shubao of this NodeIps.

        API网关shubao组件节点ip列表

        :param shubao: The shubao of this NodeIps.
        :type shubao: list[str]
        """
        self._shubao = shubao

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
        if not isinstance(other, NodeIps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
