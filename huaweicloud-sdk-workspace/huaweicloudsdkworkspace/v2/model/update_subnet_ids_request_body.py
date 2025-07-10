# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSubnetIdsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subnet_ids': 'list[str]',
        'vpc_config_infos': 'list[VpcConfigInfo]'
    }

    attribute_map = {
        'subnet_ids': 'subnet_ids',
        'vpc_config_infos': 'vpc_config_infos'
    }

    def __init__(self, subnet_ids=None, vpc_config_infos=None):
        r"""UpdateSubnetIdsRequestBody

        The model defined in huaweicloud sdk

        :param subnet_ids: 业务子网id。
        :type subnet_ids: list[str]
        :param vpc_config_infos: VPC配置信息列表。
        :type vpc_config_infos: list[:class:`huaweicloudsdkworkspace.v2.VpcConfigInfo`]
        """
        
        

        self._subnet_ids = None
        self._vpc_config_infos = None
        self.discriminator = None

        if subnet_ids is not None:
            self.subnet_ids = subnet_ids
        if vpc_config_infos is not None:
            self.vpc_config_infos = vpc_config_infos

    @property
    def subnet_ids(self):
        r"""Gets the subnet_ids of this UpdateSubnetIdsRequestBody.

        业务子网id。

        :return: The subnet_ids of this UpdateSubnetIdsRequestBody.
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        r"""Sets the subnet_ids of this UpdateSubnetIdsRequestBody.

        业务子网id。

        :param subnet_ids: The subnet_ids of this UpdateSubnetIdsRequestBody.
        :type subnet_ids: list[str]
        """
        self._subnet_ids = subnet_ids

    @property
    def vpc_config_infos(self):
        r"""Gets the vpc_config_infos of this UpdateSubnetIdsRequestBody.

        VPC配置信息列表。

        :return: The vpc_config_infos of this UpdateSubnetIdsRequestBody.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.VpcConfigInfo`]
        """
        return self._vpc_config_infos

    @vpc_config_infos.setter
    def vpc_config_infos(self, vpc_config_infos):
        r"""Sets the vpc_config_infos of this UpdateSubnetIdsRequestBody.

        VPC配置信息列表。

        :param vpc_config_infos: The vpc_config_infos of this UpdateSubnetIdsRequestBody.
        :type vpc_config_infos: list[:class:`huaweicloudsdkworkspace.v2.VpcConfigInfo`]
        """
        self._vpc_config_infos = vpc_config_infos

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
        if not isinstance(other, UpdateSubnetIdsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
