# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'used_subnet_ids': 'list[str]',
        'vpc_id': 'str',
        'subnet_ids': 'list[str]',
        'default_access_vpc': 'bool'
    }

    attribute_map = {
        'used_subnet_ids': 'used_subnet_ids',
        'vpc_id': 'vpc_id',
        'subnet_ids': 'subnet_ids',
        'default_access_vpc': 'default_access_vpc'
    }

    def __init__(self, used_subnet_ids=None, vpc_id=None, subnet_ids=None, default_access_vpc=None):
        r"""VpcConfigInfo

        The model defined in huaweicloud sdk

        :param used_subnet_ids: 已使用的子网信息。
        :type used_subnet_ids: list[str]
        :param vpc_id: VPC ID。
        :type vpc_id: str
        :param subnet_ids: 子网ID列表。
        :type subnet_ids: list[str]
        :param default_access_vpc: 是否为默认接入VPC。
        :type default_access_vpc: bool
        """
        
        

        self._used_subnet_ids = None
        self._vpc_id = None
        self._subnet_ids = None
        self._default_access_vpc = None
        self.discriminator = None

        if used_subnet_ids is not None:
            self.used_subnet_ids = used_subnet_ids
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_ids is not None:
            self.subnet_ids = subnet_ids
        if default_access_vpc is not None:
            self.default_access_vpc = default_access_vpc

    @property
    def used_subnet_ids(self):
        r"""Gets the used_subnet_ids of this VpcConfigInfo.

        已使用的子网信息。

        :return: The used_subnet_ids of this VpcConfigInfo.
        :rtype: list[str]
        """
        return self._used_subnet_ids

    @used_subnet_ids.setter
    def used_subnet_ids(self, used_subnet_ids):
        r"""Sets the used_subnet_ids of this VpcConfigInfo.

        已使用的子网信息。

        :param used_subnet_ids: The used_subnet_ids of this VpcConfigInfo.
        :type used_subnet_ids: list[str]
        """
        self._used_subnet_ids = used_subnet_ids

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this VpcConfigInfo.

        VPC ID。

        :return: The vpc_id of this VpcConfigInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this VpcConfigInfo.

        VPC ID。

        :param vpc_id: The vpc_id of this VpcConfigInfo.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_ids(self):
        r"""Gets the subnet_ids of this VpcConfigInfo.

        子网ID列表。

        :return: The subnet_ids of this VpcConfigInfo.
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        r"""Sets the subnet_ids of this VpcConfigInfo.

        子网ID列表。

        :param subnet_ids: The subnet_ids of this VpcConfigInfo.
        :type subnet_ids: list[str]
        """
        self._subnet_ids = subnet_ids

    @property
    def default_access_vpc(self):
        r"""Gets the default_access_vpc of this VpcConfigInfo.

        是否为默认接入VPC。

        :return: The default_access_vpc of this VpcConfigInfo.
        :rtype: bool
        """
        return self._default_access_vpc

    @default_access_vpc.setter
    def default_access_vpc(self, default_access_vpc):
        r"""Sets the default_access_vpc of this VpcConfigInfo.

        是否为默认接入VPC。

        :param default_access_vpc: The default_access_vpc of this VpcConfigInfo.
        :type default_access_vpc: bool
        """
        self._default_access_vpc = default_access_vpc

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
        if not isinstance(other, VpcConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
