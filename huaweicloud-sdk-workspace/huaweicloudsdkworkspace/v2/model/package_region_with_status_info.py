# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PackageRegionWithStatusInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'upload_status': 'UploadStatusEnum'
    }

    attribute_map = {
        'region': 'region',
        'upload_status': 'upload_status'
    }

    def __init__(self, region=None, upload_status=None):
        r"""PackageRegionWithStatusInfo

        The model defined in huaweicloud sdk

        :param region: 区域标识（如 cn-north-7）。
        :type region: str
        :param upload_status: 
        :type upload_status: :class:`huaweicloudsdkworkspace.v2.UploadStatusEnum`
        """
        
        

        self._region = None
        self._upload_status = None
        self.discriminator = None

        self.region = region
        self.upload_status = upload_status

    @property
    def region(self):
        r"""Gets the region of this PackageRegionWithStatusInfo.

        区域标识（如 cn-north-7）。

        :return: The region of this PackageRegionWithStatusInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this PackageRegionWithStatusInfo.

        区域标识（如 cn-north-7）。

        :param region: The region of this PackageRegionWithStatusInfo.
        :type region: str
        """
        self._region = region

    @property
    def upload_status(self):
        r"""Gets the upload_status of this PackageRegionWithStatusInfo.

        :return: The upload_status of this PackageRegionWithStatusInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.UploadStatusEnum`
        """
        return self._upload_status

    @upload_status.setter
    def upload_status(self, upload_status):
        r"""Sets the upload_status of this PackageRegionWithStatusInfo.

        :param upload_status: The upload_status of this PackageRegionWithStatusInfo.
        :type upload_status: :class:`huaweicloudsdkworkspace.v2.UploadStatusEnum`
        """
        self._upload_status = upload_status

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
        if not isinstance(other, PackageRegionWithStatusInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
