# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeployFactoryPackagesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'package_ids': 'list[str]',
        'startup_mode': 'int'
    }

    attribute_map = {
        'package_ids': 'package_ids',
        'startup_mode': 'startup_mode'
    }

    def __init__(self, package_ids=None, startup_mode=None):
        r"""DeployFactoryPackagesRequestBody

        The model defined in huaweicloud sdk

        :param package_ids: 发布包ID
        :type package_ids: list[str]
        :param startup_mode: 发布后是否立即启动作业。取值范围为0和1，默认为1, 1：发布成功后立即启动作业 0：不立即启动
        :type startup_mode: int
        """
        
        

        self._package_ids = None
        self._startup_mode = None
        self.discriminator = None

        self.package_ids = package_ids
        if startup_mode is not None:
            self.startup_mode = startup_mode

    @property
    def package_ids(self):
        r"""Gets the package_ids of this DeployFactoryPackagesRequestBody.

        发布包ID

        :return: The package_ids of this DeployFactoryPackagesRequestBody.
        :rtype: list[str]
        """
        return self._package_ids

    @package_ids.setter
    def package_ids(self, package_ids):
        r"""Sets the package_ids of this DeployFactoryPackagesRequestBody.

        发布包ID

        :param package_ids: The package_ids of this DeployFactoryPackagesRequestBody.
        :type package_ids: list[str]
        """
        self._package_ids = package_ids

    @property
    def startup_mode(self):
        r"""Gets the startup_mode of this DeployFactoryPackagesRequestBody.

        发布后是否立即启动作业。取值范围为0和1，默认为1, 1：发布成功后立即启动作业 0：不立即启动

        :return: The startup_mode of this DeployFactoryPackagesRequestBody.
        :rtype: int
        """
        return self._startup_mode

    @startup_mode.setter
    def startup_mode(self, startup_mode):
        r"""Sets the startup_mode of this DeployFactoryPackagesRequestBody.

        发布后是否立即启动作业。取值范围为0和1，默认为1, 1：发布成功后立即启动作业 0：不立即启动

        :param startup_mode: The startup_mode of this DeployFactoryPackagesRequestBody.
        :type startup_mode: int
        """
        self._startup_mode = startup_mode

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
        if not isinstance(other, DeployFactoryPackagesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
