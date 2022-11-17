# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeNicSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'primary_nic': 'NicSpec',
        'ext_nics': 'list[NicSpec]'
    }

    attribute_map = {
        'primary_nic': 'primaryNic',
        'ext_nics': 'extNics'
    }

    def __init__(self, primary_nic=None, ext_nics=None):
        """NodeNicSpec

        The model defined in huaweicloud sdk

        :param primary_nic: 
        :type primary_nic: :class:`huaweicloudsdkcce.v3.NicSpec`
        :param ext_nics: 扩展网卡 &gt;创建节点池添加节点时不支持该参数。
        :type ext_nics: list[:class:`huaweicloudsdkcce.v3.NicSpec`]
        """
        
        

        self._primary_nic = None
        self._ext_nics = None
        self.discriminator = None

        if primary_nic is not None:
            self.primary_nic = primary_nic
        if ext_nics is not None:
            self.ext_nics = ext_nics

    @property
    def primary_nic(self):
        """Gets the primary_nic of this NodeNicSpec.

        :return: The primary_nic of this NodeNicSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.NicSpec`
        """
        return self._primary_nic

    @primary_nic.setter
    def primary_nic(self, primary_nic):
        """Sets the primary_nic of this NodeNicSpec.

        :param primary_nic: The primary_nic of this NodeNicSpec.
        :type primary_nic: :class:`huaweicloudsdkcce.v3.NicSpec`
        """
        self._primary_nic = primary_nic

    @property
    def ext_nics(self):
        """Gets the ext_nics of this NodeNicSpec.

        扩展网卡 >创建节点池添加节点时不支持该参数。

        :return: The ext_nics of this NodeNicSpec.
        :rtype: list[:class:`huaweicloudsdkcce.v3.NicSpec`]
        """
        return self._ext_nics

    @ext_nics.setter
    def ext_nics(self, ext_nics):
        """Sets the ext_nics of this NodeNicSpec.

        扩展网卡 >创建节点池添加节点时不支持该参数。

        :param ext_nics: The ext_nics of this NodeNicSpec.
        :type ext_nics: list[:class:`huaweicloudsdkcce.v3.NicSpec`]
        """
        self._ext_nics = ext_nics

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
        if not isinstance(other, NodeNicSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
