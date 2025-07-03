# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateBandwidthOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'share_type': 'str',
        'size': 'int',
        'charge_mode': 'str',
        'id': 'str'
    }

    attribute_map = {
        'share_type': 'share_type',
        'size': 'size',
        'charge_mode': 'charge_mode',
        'id': 'id'
    }

    def __init__(self, share_type=None, size=None, charge_mode=None, id=None):
        r"""TemplateBandwidthOption

        The model defined in huaweicloud sdk

        :param share_type: 带宽类型
        :type share_type: str
        :param size: 带宽大小
        :type size: int
        :param charge_mode: 计费类型
        :type charge_mode: str
        :param id: 带宽ID，创建WHOLE类型带宽的弹性IP时可以指定之前的共享带宽创建
        :type id: str
        """
        
        

        self._share_type = None
        self._size = None
        self._charge_mode = None
        self._id = None
        self.discriminator = None

        if share_type is not None:
            self.share_type = share_type
        if size is not None:
            self.size = size
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if id is not None:
            self.id = id

    @property
    def share_type(self):
        r"""Gets the share_type of this TemplateBandwidthOption.

        带宽类型

        :return: The share_type of this TemplateBandwidthOption.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        r"""Sets the share_type of this TemplateBandwidthOption.

        带宽类型

        :param share_type: The share_type of this TemplateBandwidthOption.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def size(self):
        r"""Gets the size of this TemplateBandwidthOption.

        带宽大小

        :return: The size of this TemplateBandwidthOption.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this TemplateBandwidthOption.

        带宽大小

        :param size: The size of this TemplateBandwidthOption.
        :type size: int
        """
        self._size = size

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this TemplateBandwidthOption.

        计费类型

        :return: The charge_mode of this TemplateBandwidthOption.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this TemplateBandwidthOption.

        计费类型

        :param charge_mode: The charge_mode of this TemplateBandwidthOption.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def id(self):
        r"""Gets the id of this TemplateBandwidthOption.

        带宽ID，创建WHOLE类型带宽的弹性IP时可以指定之前的共享带宽创建

        :return: The id of this TemplateBandwidthOption.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TemplateBandwidthOption.

        带宽ID，创建WHOLE类型带宽的弹性IP时可以指定之前的共享带宽创建

        :param id: The id of this TemplateBandwidthOption.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, TemplateBandwidthOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
