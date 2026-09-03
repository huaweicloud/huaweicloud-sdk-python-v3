# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSkillPackageReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'package_status': 'PackageStatusEnum',
        'remark': 'str'
    }

    attribute_map = {
        'package_status': 'package_status',
        'remark': 'remark'
    }

    def __init__(self, package_status=None, remark=None):
        r"""UpdateSkillPackageReq

        The model defined in huaweicloud sdk

        :param package_status: 
        :type package_status: :class:`huaweicloudsdkworkspace.v2.PackageStatusEnum`
        :param remark: 备注。
        :type remark: str
        """
        
        

        self._package_status = None
        self._remark = None
        self.discriminator = None

        if package_status is not None:
            self.package_status = package_status
        if remark is not None:
            self.remark = remark

    @property
    def package_status(self):
        r"""Gets the package_status of this UpdateSkillPackageReq.

        :return: The package_status of this UpdateSkillPackageReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PackageStatusEnum`
        """
        return self._package_status

    @package_status.setter
    def package_status(self, package_status):
        r"""Sets the package_status of this UpdateSkillPackageReq.

        :param package_status: The package_status of this UpdateSkillPackageReq.
        :type package_status: :class:`huaweicloudsdkworkspace.v2.PackageStatusEnum`
        """
        self._package_status = package_status

    @property
    def remark(self):
        r"""Gets the remark of this UpdateSkillPackageReq.

        备注。

        :return: The remark of this UpdateSkillPackageReq.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this UpdateSkillPackageReq.

        备注。

        :param remark: The remark of this UpdateSkillPackageReq.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, UpdateSkillPackageReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
