# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMasterAddressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_name': 'str',
        'master_address': 'str'
    }

    attribute_map = {
        'region_name': 'region_name',
        'master_address': 'master_address'
    }

    def __init__(self, region_name=None, master_address=None):
        """ShowMasterAddressResponse

        The model defined in huaweicloud sdk

        :param region_name: region的英文名称。
        :type region_name: str
        :param master_address: APMmaster服务对外暴露的地址，提供服务注册和心跳上报。
        :type master_address: str
        """
        
        super(ShowMasterAddressResponse, self).__init__()

        self._region_name = None
        self._master_address = None
        self.discriminator = None

        if region_name is not None:
            self.region_name = region_name
        if master_address is not None:
            self.master_address = master_address

    @property
    def region_name(self):
        """Gets the region_name of this ShowMasterAddressResponse.

        region的英文名称。

        :return: The region_name of this ShowMasterAddressResponse.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this ShowMasterAddressResponse.

        region的英文名称。

        :param region_name: The region_name of this ShowMasterAddressResponse.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def master_address(self):
        """Gets the master_address of this ShowMasterAddressResponse.

        APMmaster服务对外暴露的地址，提供服务注册和心跳上报。

        :return: The master_address of this ShowMasterAddressResponse.
        :rtype: str
        """
        return self._master_address

    @master_address.setter
    def master_address(self, master_address):
        """Sets the master_address of this ShowMasterAddressResponse.

        APMmaster服务对外暴露的地址，提供服务注册和心跳上报。

        :param master_address: The master_address of this ShowMasterAddressResponse.
        :type master_address: str
        """
        self._master_address = master_address

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
        if not isinstance(other, ShowMasterAddressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
