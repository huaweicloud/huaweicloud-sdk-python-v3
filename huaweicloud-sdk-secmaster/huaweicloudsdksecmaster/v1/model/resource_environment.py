# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceEnvironment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vendor_type': 'str',
        'domain_id': 'str',
        'region_id': 'str',
        'project_id': 'str',
        'ep_id': 'str',
        'ep_name': 'str',
        'vendor_name': 'str',
        'idc_name': 'str',
        'idc_id': 'str'
    }

    attribute_map = {
        'vendor_type': 'vendor_type',
        'domain_id': 'domain_id',
        'region_id': 'region_id',
        'project_id': 'project_id',
        'ep_id': 'ep_id',
        'ep_name': 'ep_name',
        'vendor_name': 'vendor_name',
        'idc_name': 'idc_name',
        'idc_id': 'idc_id'
    }

    def __init__(self, vendor_type=None, domain_id=None, region_id=None, project_id=None, ep_id=None, ep_name=None, vendor_name=None, idc_name=None, idc_id=None):
        r"""ResourceEnvironment

        The model defined in huaweicloud sdk

        :param vendor_type: 环境供应商
        :type vendor_type: str
        :param domain_id: HWC special，资产归属
        :type domain_id: str
        :param region_id: HWC special，全局服务\&quot;global\&quot;，资产归属
        :type region_id: str
        :param project_id: HWC special， 全局服务默认null， 资产归属
        :type project_id: str
        :param ep_id: HWC special，资产归属的企业项目id。
        :type ep_id: str
        :param ep_name: HWC special，资产归属的企业项目名称。
        :type ep_name: str
        :param vendor_name: OCA special，包含资产探针或资产提供商
        :type vendor_name: str
        :param idc_name: OCA special，线下机房名称
        :type idc_name: str
        :param idc_id: OCA special，线下机房id
        :type idc_id: str
        """
        
        

        self._vendor_type = None
        self._domain_id = None
        self._region_id = None
        self._project_id = None
        self._ep_id = None
        self._ep_name = None
        self._vendor_name = None
        self._idc_name = None
        self._idc_id = None
        self.discriminator = None

        self.vendor_type = vendor_type
        self.domain_id = domain_id
        if region_id is not None:
            self.region_id = region_id
        if project_id is not None:
            self.project_id = project_id
        if ep_id is not None:
            self.ep_id = ep_id
        if ep_name is not None:
            self.ep_name = ep_name
        self.vendor_name = vendor_name
        self.idc_name = idc_name
        if idc_id is not None:
            self.idc_id = idc_id

    @property
    def vendor_type(self):
        r"""Gets the vendor_type of this ResourceEnvironment.

        环境供应商

        :return: The vendor_type of this ResourceEnvironment.
        :rtype: str
        """
        return self._vendor_type

    @vendor_type.setter
    def vendor_type(self, vendor_type):
        r"""Sets the vendor_type of this ResourceEnvironment.

        环境供应商

        :param vendor_type: The vendor_type of this ResourceEnvironment.
        :type vendor_type: str
        """
        self._vendor_type = vendor_type

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ResourceEnvironment.

        HWC special，资产归属

        :return: The domain_id of this ResourceEnvironment.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ResourceEnvironment.

        HWC special，资产归属

        :param domain_id: The domain_id of this ResourceEnvironment.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ResourceEnvironment.

        HWC special，全局服务\"global\"，资产归属

        :return: The region_id of this ResourceEnvironment.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ResourceEnvironment.

        HWC special，全局服务\"global\"，资产归属

        :param region_id: The region_id of this ResourceEnvironment.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ResourceEnvironment.

        HWC special， 全局服务默认null， 资产归属

        :return: The project_id of this ResourceEnvironment.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ResourceEnvironment.

        HWC special， 全局服务默认null， 资产归属

        :param project_id: The project_id of this ResourceEnvironment.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def ep_id(self):
        r"""Gets the ep_id of this ResourceEnvironment.

        HWC special，资产归属的企业项目id。

        :return: The ep_id of this ResourceEnvironment.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        r"""Sets the ep_id of this ResourceEnvironment.

        HWC special，资产归属的企业项目id。

        :param ep_id: The ep_id of this ResourceEnvironment.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def ep_name(self):
        r"""Gets the ep_name of this ResourceEnvironment.

        HWC special，资产归属的企业项目名称。

        :return: The ep_name of this ResourceEnvironment.
        :rtype: str
        """
        return self._ep_name

    @ep_name.setter
    def ep_name(self, ep_name):
        r"""Sets the ep_name of this ResourceEnvironment.

        HWC special，资产归属的企业项目名称。

        :param ep_name: The ep_name of this ResourceEnvironment.
        :type ep_name: str
        """
        self._ep_name = ep_name

    @property
    def vendor_name(self):
        r"""Gets the vendor_name of this ResourceEnvironment.

        OCA special，包含资产探针或资产提供商

        :return: The vendor_name of this ResourceEnvironment.
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        r"""Sets the vendor_name of this ResourceEnvironment.

        OCA special，包含资产探针或资产提供商

        :param vendor_name: The vendor_name of this ResourceEnvironment.
        :type vendor_name: str
        """
        self._vendor_name = vendor_name

    @property
    def idc_name(self):
        r"""Gets the idc_name of this ResourceEnvironment.

        OCA special，线下机房名称

        :return: The idc_name of this ResourceEnvironment.
        :rtype: str
        """
        return self._idc_name

    @idc_name.setter
    def idc_name(self, idc_name):
        r"""Sets the idc_name of this ResourceEnvironment.

        OCA special，线下机房名称

        :param idc_name: The idc_name of this ResourceEnvironment.
        :type idc_name: str
        """
        self._idc_name = idc_name

    @property
    def idc_id(self):
        r"""Gets the idc_id of this ResourceEnvironment.

        OCA special，线下机房id

        :return: The idc_id of this ResourceEnvironment.
        :rtype: str
        """
        return self._idc_id

    @idc_id.setter
    def idc_id(self, idc_id):
        r"""Sets the idc_id of this ResourceEnvironment.

        OCA special，线下机房id

        :param idc_id: The idc_id of this ResourceEnvironment.
        :type idc_id: str
        """
        self._idc_id = idc_id

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
        if not isinstance(other, ResourceEnvironment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
