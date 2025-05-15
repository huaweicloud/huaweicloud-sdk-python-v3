# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegionBandwidthPackageSpecification:

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
        'id': 'str',
        'name': 'str',
        'en_name': 'str',
        'es_name': 'str',
        'pt_name': 'str',
        'spec_codes': 'list[SpecificationCodeInfo]'
    }

    attribute_map = {
        'local_region_id': 'local_region_id',
        'remote_region_id': 'remote_region_id',
        'id': 'id',
        'name': 'name',
        'en_name': 'en_name',
        'es_name': 'es_name',
        'pt_name': 'pt_name',
        'spec_codes': 'spec_codes'
    }

    def __init__(self, local_region_id=None, remote_region_id=None, id=None, name=None, en_name=None, es_name=None, pt_name=None, spec_codes=None):
        r"""RegionBandwidthPackageSpecification

        The model defined in huaweicloud sdk

        :param local_region_id: RegionID。
        :type local_region_id: str
        :param remote_region_id: RegionID。
        :type remote_region_id: str
        :param id: 互通Region带宽包的规格ID。
        :type id: str
        :param name: 互通Region带宽包的规格名字。
        :type name: str
        :param en_name: 互通Region带宽包的规格英文名字。
        :type en_name: str
        :param es_name: 互通Region带宽包的规格西语名字。
        :type es_name: str
        :param pt_name: 互通Region带宽包的规格葡语名字。
        :type pt_name: str
        :param spec_codes: 带宽包产品规格列表。
        :type spec_codes: list[:class:`huaweicloudsdkcc.v3.SpecificationCodeInfo`]
        """
        
        

        self._local_region_id = None
        self._remote_region_id = None
        self._id = None
        self._name = None
        self._en_name = None
        self._es_name = None
        self._pt_name = None
        self._spec_codes = None
        self.discriminator = None

        self.local_region_id = local_region_id
        self.remote_region_id = remote_region_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if en_name is not None:
            self.en_name = en_name
        if es_name is not None:
            self.es_name = es_name
        if pt_name is not None:
            self.pt_name = pt_name
        if spec_codes is not None:
            self.spec_codes = spec_codes

    @property
    def local_region_id(self):
        r"""Gets the local_region_id of this RegionBandwidthPackageSpecification.

        RegionID。

        :return: The local_region_id of this RegionBandwidthPackageSpecification.
        :rtype: str
        """
        return self._local_region_id

    @local_region_id.setter
    def local_region_id(self, local_region_id):
        r"""Sets the local_region_id of this RegionBandwidthPackageSpecification.

        RegionID。

        :param local_region_id: The local_region_id of this RegionBandwidthPackageSpecification.
        :type local_region_id: str
        """
        self._local_region_id = local_region_id

    @property
    def remote_region_id(self):
        r"""Gets the remote_region_id of this RegionBandwidthPackageSpecification.

        RegionID。

        :return: The remote_region_id of this RegionBandwidthPackageSpecification.
        :rtype: str
        """
        return self._remote_region_id

    @remote_region_id.setter
    def remote_region_id(self, remote_region_id):
        r"""Sets the remote_region_id of this RegionBandwidthPackageSpecification.

        RegionID。

        :param remote_region_id: The remote_region_id of this RegionBandwidthPackageSpecification.
        :type remote_region_id: str
        """
        self._remote_region_id = remote_region_id

    @property
    def id(self):
        r"""Gets the id of this RegionBandwidthPackageSpecification.

        互通Region带宽包的规格ID。

        :return: The id of this RegionBandwidthPackageSpecification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RegionBandwidthPackageSpecification.

        互通Region带宽包的规格ID。

        :param id: The id of this RegionBandwidthPackageSpecification.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this RegionBandwidthPackageSpecification.

        互通Region带宽包的规格名字。

        :return: The name of this RegionBandwidthPackageSpecification.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RegionBandwidthPackageSpecification.

        互通Region带宽包的规格名字。

        :param name: The name of this RegionBandwidthPackageSpecification.
        :type name: str
        """
        self._name = name

    @property
    def en_name(self):
        r"""Gets the en_name of this RegionBandwidthPackageSpecification.

        互通Region带宽包的规格英文名字。

        :return: The en_name of this RegionBandwidthPackageSpecification.
        :rtype: str
        """
        return self._en_name

    @en_name.setter
    def en_name(self, en_name):
        r"""Sets the en_name of this RegionBandwidthPackageSpecification.

        互通Region带宽包的规格英文名字。

        :param en_name: The en_name of this RegionBandwidthPackageSpecification.
        :type en_name: str
        """
        self._en_name = en_name

    @property
    def es_name(self):
        r"""Gets the es_name of this RegionBandwidthPackageSpecification.

        互通Region带宽包的规格西语名字。

        :return: The es_name of this RegionBandwidthPackageSpecification.
        :rtype: str
        """
        return self._es_name

    @es_name.setter
    def es_name(self, es_name):
        r"""Sets the es_name of this RegionBandwidthPackageSpecification.

        互通Region带宽包的规格西语名字。

        :param es_name: The es_name of this RegionBandwidthPackageSpecification.
        :type es_name: str
        """
        self._es_name = es_name

    @property
    def pt_name(self):
        r"""Gets the pt_name of this RegionBandwidthPackageSpecification.

        互通Region带宽包的规格葡语名字。

        :return: The pt_name of this RegionBandwidthPackageSpecification.
        :rtype: str
        """
        return self._pt_name

    @pt_name.setter
    def pt_name(self, pt_name):
        r"""Sets the pt_name of this RegionBandwidthPackageSpecification.

        互通Region带宽包的规格葡语名字。

        :param pt_name: The pt_name of this RegionBandwidthPackageSpecification.
        :type pt_name: str
        """
        self._pt_name = pt_name

    @property
    def spec_codes(self):
        r"""Gets the spec_codes of this RegionBandwidthPackageSpecification.

        带宽包产品规格列表。

        :return: The spec_codes of this RegionBandwidthPackageSpecification.
        :rtype: list[:class:`huaweicloudsdkcc.v3.SpecificationCodeInfo`]
        """
        return self._spec_codes

    @spec_codes.setter
    def spec_codes(self, spec_codes):
        r"""Sets the spec_codes of this RegionBandwidthPackageSpecification.

        带宽包产品规格列表。

        :param spec_codes: The spec_codes of this RegionBandwidthPackageSpecification.
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
        if not isinstance(other, RegionBandwidthPackageSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
