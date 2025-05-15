# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BandwidthPackageLine:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'local_region_id': 'str',
        'remote_region_id': 'str',
        'local_site_code': 'str',
        'remote_site_code': 'str',
        'support_levels': 'list[str]',
        'spec_codes': 'list[BandwidthPackageLineSpecCode]'
    }

    attribute_map = {
        'local_region_id': 'local_region_id',
        'remote_region_id': 'remote_region_id',
        'local_site_code': 'local_site_code',
        'remote_site_code': 'remote_site_code',
        'support_levels': 'support_levels',
        'spec_codes': 'spec_codes'
    }

    def __init__(self, local_region_id=None, remote_region_id=None, local_site_code=None, remote_site_code=None, support_levels=None, spec_codes=None):
        r"""BandwidthPackageLine

        The model defined in huaweicloud sdk

        :param local_region_id: RegionID。
        :type local_region_id: str
        :param remote_region_id: RegionID。
        :type remote_region_id: str
        :param local_site_code: 站点编码。
        :type local_site_code: str
        :param remote_site_code: 站点编码。
        :type remote_site_code: str
        :param support_levels: 支持的等级列表。
        :type support_levels: list[str]
        :param spec_codes: 产品编码列表。
        :type spec_codes: list[:class:`huaweicloudsdkcc.v3.BandwidthPackageLineSpecCode`]
        """
        
        

        self._local_region_id = None
        self._remote_region_id = None
        self._local_site_code = None
        self._remote_site_code = None
        self._support_levels = None
        self._spec_codes = None
        self.discriminator = None

        if local_region_id is not None:
            self.local_region_id = local_region_id
        if remote_region_id is not None:
            self.remote_region_id = remote_region_id
        if local_site_code is not None:
            self.local_site_code = local_site_code
        if remote_site_code is not None:
            self.remote_site_code = remote_site_code
        if support_levels is not None:
            self.support_levels = support_levels
        if spec_codes is not None:
            self.spec_codes = spec_codes

    @property
    def local_region_id(self):
        r"""Gets the local_region_id of this BandwidthPackageLine.

        RegionID。

        :return: The local_region_id of this BandwidthPackageLine.
        :rtype: str
        """
        return self._local_region_id

    @local_region_id.setter
    def local_region_id(self, local_region_id):
        r"""Sets the local_region_id of this BandwidthPackageLine.

        RegionID。

        :param local_region_id: The local_region_id of this BandwidthPackageLine.
        :type local_region_id: str
        """
        self._local_region_id = local_region_id

    @property
    def remote_region_id(self):
        r"""Gets the remote_region_id of this BandwidthPackageLine.

        RegionID。

        :return: The remote_region_id of this BandwidthPackageLine.
        :rtype: str
        """
        return self._remote_region_id

    @remote_region_id.setter
    def remote_region_id(self, remote_region_id):
        r"""Sets the remote_region_id of this BandwidthPackageLine.

        RegionID。

        :param remote_region_id: The remote_region_id of this BandwidthPackageLine.
        :type remote_region_id: str
        """
        self._remote_region_id = remote_region_id

    @property
    def local_site_code(self):
        r"""Gets the local_site_code of this BandwidthPackageLine.

        站点编码。

        :return: The local_site_code of this BandwidthPackageLine.
        :rtype: str
        """
        return self._local_site_code

    @local_site_code.setter
    def local_site_code(self, local_site_code):
        r"""Sets the local_site_code of this BandwidthPackageLine.

        站点编码。

        :param local_site_code: The local_site_code of this BandwidthPackageLine.
        :type local_site_code: str
        """
        self._local_site_code = local_site_code

    @property
    def remote_site_code(self):
        r"""Gets the remote_site_code of this BandwidthPackageLine.

        站点编码。

        :return: The remote_site_code of this BandwidthPackageLine.
        :rtype: str
        """
        return self._remote_site_code

    @remote_site_code.setter
    def remote_site_code(self, remote_site_code):
        r"""Sets the remote_site_code of this BandwidthPackageLine.

        站点编码。

        :param remote_site_code: The remote_site_code of this BandwidthPackageLine.
        :type remote_site_code: str
        """
        self._remote_site_code = remote_site_code

    @property
    def support_levels(self):
        r"""Gets the support_levels of this BandwidthPackageLine.

        支持的等级列表。

        :return: The support_levels of this BandwidthPackageLine.
        :rtype: list[str]
        """
        return self._support_levels

    @support_levels.setter
    def support_levels(self, support_levels):
        r"""Sets the support_levels of this BandwidthPackageLine.

        支持的等级列表。

        :param support_levels: The support_levels of this BandwidthPackageLine.
        :type support_levels: list[str]
        """
        self._support_levels = support_levels

    @property
    def spec_codes(self):
        r"""Gets the spec_codes of this BandwidthPackageLine.

        产品编码列表。

        :return: The spec_codes of this BandwidthPackageLine.
        :rtype: list[:class:`huaweicloudsdkcc.v3.BandwidthPackageLineSpecCode`]
        """
        return self._spec_codes

    @spec_codes.setter
    def spec_codes(self, spec_codes):
        r"""Sets the spec_codes of this BandwidthPackageLine.

        产品编码列表。

        :param spec_codes: The spec_codes of this BandwidthPackageLine.
        :type spec_codes: list[:class:`huaweicloudsdkcc.v3.BandwidthPackageLineSpecCode`]
        """
        self._spec_codes = spec_codes

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
        if not isinstance(other, BandwidthPackageLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
