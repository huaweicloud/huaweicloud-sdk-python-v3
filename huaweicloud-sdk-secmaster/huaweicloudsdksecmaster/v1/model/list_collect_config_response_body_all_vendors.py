# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCollectConfigResponseBodyAllVendors:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_vendor': 'str',
        'csvc_list': 'list[ListCollectConfigResponseBodyCsvcList]'
    }

    attribute_map = {
        'cloud_vendor': 'cloud_vendor',
        'csvc_list': 'csvc_list'
    }

    def __init__(self, cloud_vendor=None, csvc_list=None):
        r"""ListCollectConfigResponseBodyAllVendors

        The model defined in huaweicloud sdk

        :param cloud_vendor: 云厂商ID
        :type cloud_vendor: str
        :param csvc_list: 所有的云产品
        :type csvc_list: list[:class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyCsvcList`]
        """
        
        

        self._cloud_vendor = None
        self._csvc_list = None
        self.discriminator = None

        if cloud_vendor is not None:
            self.cloud_vendor = cloud_vendor
        if csvc_list is not None:
            self.csvc_list = csvc_list

    @property
    def cloud_vendor(self):
        r"""Gets the cloud_vendor of this ListCollectConfigResponseBodyAllVendors.

        云厂商ID

        :return: The cloud_vendor of this ListCollectConfigResponseBodyAllVendors.
        :rtype: str
        """
        return self._cloud_vendor

    @cloud_vendor.setter
    def cloud_vendor(self, cloud_vendor):
        r"""Sets the cloud_vendor of this ListCollectConfigResponseBodyAllVendors.

        云厂商ID

        :param cloud_vendor: The cloud_vendor of this ListCollectConfigResponseBodyAllVendors.
        :type cloud_vendor: str
        """
        self._cloud_vendor = cloud_vendor

    @property
    def csvc_list(self):
        r"""Gets the csvc_list of this ListCollectConfigResponseBodyAllVendors.

        所有的云产品

        :return: The csvc_list of this ListCollectConfigResponseBodyAllVendors.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyCsvcList`]
        """
        return self._csvc_list

    @csvc_list.setter
    def csvc_list(self, csvc_list):
        r"""Sets the csvc_list of this ListCollectConfigResponseBodyAllVendors.

        所有的云产品

        :param csvc_list: The csvc_list of this ListCollectConfigResponseBodyAllVendors.
        :type csvc_list: list[:class:`huaweicloudsdksecmaster.v1.ListCollectConfigResponseBodyCsvcList`]
        """
        self._csvc_list = csvc_list

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
        if not isinstance(other, ListCollectConfigResponseBodyAllVendors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
