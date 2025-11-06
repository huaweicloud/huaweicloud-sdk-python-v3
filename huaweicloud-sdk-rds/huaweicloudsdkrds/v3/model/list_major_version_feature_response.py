# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMajorVersionFeatureResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'support_upgrade_version': 'list[str]',
        'support_recover_version': 'list[str]',
        'support_file_stream': 'bool',
        'support_tde': 'bool',
        'support_always_on': 'bool',
        'support_read_only': 'bool'
    }

    attribute_map = {
        'version': 'version',
        'support_upgrade_version': 'support_upgrade_version',
        'support_recover_version': 'support_recover_version',
        'support_file_stream': 'support_file_stream',
        'support_tde': 'support_tde',
        'support_always_on': 'support_always_on',
        'support_read_only': 'support_read_only'
    }

    def __init__(self, version=None, support_upgrade_version=None, support_recover_version=None, support_file_stream=None, support_tde=None, support_always_on=None, support_read_only=None):
        r"""ListMajorVersionFeatureResponse

        The model defined in huaweicloud sdk

        :param version: 版本名称。
        :type version: str
        :param support_upgrade_version: 支持升级的版本列表。
        :type support_upgrade_version: list[str]
        :param support_recover_version: 支持备份恢复的版本列表。
        :type support_recover_version: list[str]
        :param support_file_stream: 是否支持FileStream特性。
        :type support_file_stream: bool
        :param support_tde: 是否支持透明数据加密。
        :type support_tde: bool
        :param support_always_on: 是否支持Always On。
        :type support_always_on: bool
        :param support_read_only: 是否支持只读。
        :type support_read_only: bool
        """
        
        super().__init__()

        self._version = None
        self._support_upgrade_version = None
        self._support_recover_version = None
        self._support_file_stream = None
        self._support_tde = None
        self._support_always_on = None
        self._support_read_only = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if support_upgrade_version is not None:
            self.support_upgrade_version = support_upgrade_version
        if support_recover_version is not None:
            self.support_recover_version = support_recover_version
        if support_file_stream is not None:
            self.support_file_stream = support_file_stream
        if support_tde is not None:
            self.support_tde = support_tde
        if support_always_on is not None:
            self.support_always_on = support_always_on
        if support_read_only is not None:
            self.support_read_only = support_read_only

    @property
    def version(self):
        r"""Gets the version of this ListMajorVersionFeatureResponse.

        版本名称。

        :return: The version of this ListMajorVersionFeatureResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListMajorVersionFeatureResponse.

        版本名称。

        :param version: The version of this ListMajorVersionFeatureResponse.
        :type version: str
        """
        self._version = version

    @property
    def support_upgrade_version(self):
        r"""Gets the support_upgrade_version of this ListMajorVersionFeatureResponse.

        支持升级的版本列表。

        :return: The support_upgrade_version of this ListMajorVersionFeatureResponse.
        :rtype: list[str]
        """
        return self._support_upgrade_version

    @support_upgrade_version.setter
    def support_upgrade_version(self, support_upgrade_version):
        r"""Sets the support_upgrade_version of this ListMajorVersionFeatureResponse.

        支持升级的版本列表。

        :param support_upgrade_version: The support_upgrade_version of this ListMajorVersionFeatureResponse.
        :type support_upgrade_version: list[str]
        """
        self._support_upgrade_version = support_upgrade_version

    @property
    def support_recover_version(self):
        r"""Gets the support_recover_version of this ListMajorVersionFeatureResponse.

        支持备份恢复的版本列表。

        :return: The support_recover_version of this ListMajorVersionFeatureResponse.
        :rtype: list[str]
        """
        return self._support_recover_version

    @support_recover_version.setter
    def support_recover_version(self, support_recover_version):
        r"""Sets the support_recover_version of this ListMajorVersionFeatureResponse.

        支持备份恢复的版本列表。

        :param support_recover_version: The support_recover_version of this ListMajorVersionFeatureResponse.
        :type support_recover_version: list[str]
        """
        self._support_recover_version = support_recover_version

    @property
    def support_file_stream(self):
        r"""Gets the support_file_stream of this ListMajorVersionFeatureResponse.

        是否支持FileStream特性。

        :return: The support_file_stream of this ListMajorVersionFeatureResponse.
        :rtype: bool
        """
        return self._support_file_stream

    @support_file_stream.setter
    def support_file_stream(self, support_file_stream):
        r"""Sets the support_file_stream of this ListMajorVersionFeatureResponse.

        是否支持FileStream特性。

        :param support_file_stream: The support_file_stream of this ListMajorVersionFeatureResponse.
        :type support_file_stream: bool
        """
        self._support_file_stream = support_file_stream

    @property
    def support_tde(self):
        r"""Gets the support_tde of this ListMajorVersionFeatureResponse.

        是否支持透明数据加密。

        :return: The support_tde of this ListMajorVersionFeatureResponse.
        :rtype: bool
        """
        return self._support_tde

    @support_tde.setter
    def support_tde(self, support_tde):
        r"""Sets the support_tde of this ListMajorVersionFeatureResponse.

        是否支持透明数据加密。

        :param support_tde: The support_tde of this ListMajorVersionFeatureResponse.
        :type support_tde: bool
        """
        self._support_tde = support_tde

    @property
    def support_always_on(self):
        r"""Gets the support_always_on of this ListMajorVersionFeatureResponse.

        是否支持Always On。

        :return: The support_always_on of this ListMajorVersionFeatureResponse.
        :rtype: bool
        """
        return self._support_always_on

    @support_always_on.setter
    def support_always_on(self, support_always_on):
        r"""Sets the support_always_on of this ListMajorVersionFeatureResponse.

        是否支持Always On。

        :param support_always_on: The support_always_on of this ListMajorVersionFeatureResponse.
        :type support_always_on: bool
        """
        self._support_always_on = support_always_on

    @property
    def support_read_only(self):
        r"""Gets the support_read_only of this ListMajorVersionFeatureResponse.

        是否支持只读。

        :return: The support_read_only of this ListMajorVersionFeatureResponse.
        :rtype: bool
        """
        return self._support_read_only

    @support_read_only.setter
    def support_read_only(self, support_read_only):
        r"""Sets the support_read_only of this ListMajorVersionFeatureResponse.

        是否支持只读。

        :param support_read_only: The support_read_only of this ListMajorVersionFeatureResponse.
        :type support_read_only: bool
        """
        self._support_read_only = support_read_only

    def to_dict(self):
        import warnings
        warnings.warn("ListMajorVersionFeatureResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListMajorVersionFeatureResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
