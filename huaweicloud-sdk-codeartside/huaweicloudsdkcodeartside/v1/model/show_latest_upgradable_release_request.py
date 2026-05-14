# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLatestUpgradableReleaseRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_product_name': 'str',
        'os_type': 'str',
        'arch': 'str'
    }

    attribute_map = {
        'sub_product_name': 'sub_product_name',
        'os_type': 'os_type',
        'arch': 'arch'
    }

    def __init__(self, sub_product_name=None, os_type=None, arch=None):
        r"""ShowLatestUpgradableReleaseRequest

        The model defined in huaweicloud sdk

        :param sub_product_name: 子产品名称
        :type sub_product_name: str
        :param os_type: 系统类型
        :type os_type: str
        :param arch: CPU架构
        :type arch: str
        """
        
        

        self._sub_product_name = None
        self._os_type = None
        self._arch = None
        self.discriminator = None

        self.sub_product_name = sub_product_name
        self.os_type = os_type
        if arch is not None:
            self.arch = arch

    @property
    def sub_product_name(self):
        r"""Gets the sub_product_name of this ShowLatestUpgradableReleaseRequest.

        子产品名称

        :return: The sub_product_name of this ShowLatestUpgradableReleaseRequest.
        :rtype: str
        """
        return self._sub_product_name

    @sub_product_name.setter
    def sub_product_name(self, sub_product_name):
        r"""Sets the sub_product_name of this ShowLatestUpgradableReleaseRequest.

        子产品名称

        :param sub_product_name: The sub_product_name of this ShowLatestUpgradableReleaseRequest.
        :type sub_product_name: str
        """
        self._sub_product_name = sub_product_name

    @property
    def os_type(self):
        r"""Gets the os_type of this ShowLatestUpgradableReleaseRequest.

        系统类型

        :return: The os_type of this ShowLatestUpgradableReleaseRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ShowLatestUpgradableReleaseRequest.

        系统类型

        :param os_type: The os_type of this ShowLatestUpgradableReleaseRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def arch(self):
        r"""Gets the arch of this ShowLatestUpgradableReleaseRequest.

        CPU架构

        :return: The arch of this ShowLatestUpgradableReleaseRequest.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this ShowLatestUpgradableReleaseRequest.

        CPU架构

        :param arch: The arch of this ShowLatestUpgradableReleaseRequest.
        :type arch: str
        """
        self._arch = arch

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowLatestUpgradableReleaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
