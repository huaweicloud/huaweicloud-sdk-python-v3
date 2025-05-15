# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AreaBandwidthPackageSpecification:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'local_area_id': 'AreaIdDef',
        'remote_area_id': 'AreaIdDef',
        'id': 'str',
        'spec_codes': 'list[SpecificationCodeInfo]'
    }

    attribute_map = {
        'local_area_id': 'local_area_id',
        'remote_area_id': 'remote_area_id',
        'id': 'id',
        'spec_codes': 'spec_codes'
    }

    def __init__(self, local_area_id=None, remote_area_id=None, id=None, spec_codes=None):
        r"""AreaBandwidthPackageSpecification

        The model defined in huaweicloud sdk

        :param local_area_id: 
        :type local_area_id: :class:`huaweicloudsdkcc.v3.AreaIdDef`
        :param remote_area_id: 
        :type remote_area_id: :class:`huaweicloudsdkcc.v3.AreaIdDef`
        :param id: 互通大区带宽包的规格ID。
        :type id: str
        :param spec_codes: 带宽包产品规格列表。
        :type spec_codes: list[:class:`huaweicloudsdkcc.v3.SpecificationCodeInfo`]
        """
        
        

        self._local_area_id = None
        self._remote_area_id = None
        self._id = None
        self._spec_codes = None
        self.discriminator = None

        self.local_area_id = local_area_id
        self.remote_area_id = remote_area_id
        self.id = id
        self.spec_codes = spec_codes

    @property
    def local_area_id(self):
        r"""Gets the local_area_id of this AreaBandwidthPackageSpecification.

        :return: The local_area_id of this AreaBandwidthPackageSpecification.
        :rtype: :class:`huaweicloudsdkcc.v3.AreaIdDef`
        """
        return self._local_area_id

    @local_area_id.setter
    def local_area_id(self, local_area_id):
        r"""Sets the local_area_id of this AreaBandwidthPackageSpecification.

        :param local_area_id: The local_area_id of this AreaBandwidthPackageSpecification.
        :type local_area_id: :class:`huaweicloudsdkcc.v3.AreaIdDef`
        """
        self._local_area_id = local_area_id

    @property
    def remote_area_id(self):
        r"""Gets the remote_area_id of this AreaBandwidthPackageSpecification.

        :return: The remote_area_id of this AreaBandwidthPackageSpecification.
        :rtype: :class:`huaweicloudsdkcc.v3.AreaIdDef`
        """
        return self._remote_area_id

    @remote_area_id.setter
    def remote_area_id(self, remote_area_id):
        r"""Sets the remote_area_id of this AreaBandwidthPackageSpecification.

        :param remote_area_id: The remote_area_id of this AreaBandwidthPackageSpecification.
        :type remote_area_id: :class:`huaweicloudsdkcc.v3.AreaIdDef`
        """
        self._remote_area_id = remote_area_id

    @property
    def id(self):
        r"""Gets the id of this AreaBandwidthPackageSpecification.

        互通大区带宽包的规格ID。

        :return: The id of this AreaBandwidthPackageSpecification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AreaBandwidthPackageSpecification.

        互通大区带宽包的规格ID。

        :param id: The id of this AreaBandwidthPackageSpecification.
        :type id: str
        """
        self._id = id

    @property
    def spec_codes(self):
        r"""Gets the spec_codes of this AreaBandwidthPackageSpecification.

        带宽包产品规格列表。

        :return: The spec_codes of this AreaBandwidthPackageSpecification.
        :rtype: list[:class:`huaweicloudsdkcc.v3.SpecificationCodeInfo`]
        """
        return self._spec_codes

    @spec_codes.setter
    def spec_codes(self, spec_codes):
        r"""Sets the spec_codes of this AreaBandwidthPackageSpecification.

        带宽包产品规格列表。

        :param spec_codes: The spec_codes of this AreaBandwidthPackageSpecification.
        :type spec_codes: list[:class:`huaweicloudsdkcc.v3.SpecificationCodeInfo`]
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
        if not isinstance(other, AreaBandwidthPackageSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
