# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class V2NetworkBriefInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'cidr_in_vpc': 'str',
        'create_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'cidr_in_vpc': 'cidr_in_vpc',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, cidr_in_vpc=None, create_time=None):
        r"""V2NetworkBriefInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**：网络连接的ID。 **取值范围**：长度为1~64的英文、数字、中划线组合。 
        :type id: str
        :param cidr_in_vpc: **参数解释**：路由网段范围，标准的IPv4格式。 **取值范围**：允许网段为10.0.0.0~10.255.0.0/8~22,172.16.0.0~172.31.0.0/12~22,192.168.0.0~192.168.0.0/16~22。 
        :type cidr_in_vpc: str
        :param create_time: **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ，UTC时间。 
        :type create_time: datetime
        """
        
        

        self._id = None
        self._cidr_in_vpc = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cidr_in_vpc is not None:
            self.cidr_in_vpc = cidr_in_vpc
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        r"""Gets the id of this V2NetworkBriefInfo.

        **参数解释**：网络连接的ID。 **取值范围**：长度为1~64的英文、数字、中划线组合。 

        :return: The id of this V2NetworkBriefInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this V2NetworkBriefInfo.

        **参数解释**：网络连接的ID。 **取值范围**：长度为1~64的英文、数字、中划线组合。 

        :param id: The id of this V2NetworkBriefInfo.
        :type id: str
        """
        self._id = id

    @property
    def cidr_in_vpc(self):
        r"""Gets the cidr_in_vpc of this V2NetworkBriefInfo.

        **参数解释**：路由网段范围，标准的IPv4格式。 **取值范围**：允许网段为10.0.0.0~10.255.0.0/8~22,172.16.0.0~172.31.0.0/12~22,192.168.0.0~192.168.0.0/16~22。 

        :return: The cidr_in_vpc of this V2NetworkBriefInfo.
        :rtype: str
        """
        return self._cidr_in_vpc

    @cidr_in_vpc.setter
    def cidr_in_vpc(self, cidr_in_vpc):
        r"""Sets the cidr_in_vpc of this V2NetworkBriefInfo.

        **参数解释**：路由网段范围，标准的IPv4格式。 **取值范围**：允许网段为10.0.0.0~10.255.0.0/8~22,172.16.0.0~172.31.0.0/12~22,192.168.0.0~192.168.0.0/16~22。 

        :param cidr_in_vpc: The cidr_in_vpc of this V2NetworkBriefInfo.
        :type cidr_in_vpc: str
        """
        self._cidr_in_vpc = cidr_in_vpc

    @property
    def create_time(self):
        r"""Gets the create_time of this V2NetworkBriefInfo.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :return: The create_time of this V2NetworkBriefInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this V2NetworkBriefInfo.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :param create_time: The create_time of this V2NetworkBriefInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

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
        if not isinstance(other, V2NetworkBriefInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
