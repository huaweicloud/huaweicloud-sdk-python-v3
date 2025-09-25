# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetResourceRsp:

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
        'resource_id': 'str',
        'spec_code': 'str',
        'charge_mode': 'str',
        'status': 'AssetResourceStatusEnum',
        'create_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'resource_id': 'resource_id',
        'spec_code': 'spec_code',
        'charge_mode': 'charge_mode',
        'status': 'status',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, resource_id=None, spec_code=None, charge_mode=None, status=None, create_time=None):
        r"""AssetResourceRsp

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 实例ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type id: str
        :param resource_id: **参数解释**： 资源ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type resource_id: str
        :param spec_code: **参数解释**： 规格信息。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type spec_code: str
        :param charge_mode: **参数解释**： 计费类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type charge_mode: str
        :param status: 
        :type status: :class:`huaweicloudsdkeihealth.v1.AssetResourceStatusEnum`
        :param create_time: **参数解释**： 购买时间，UTC时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type create_time: str
        """
        
        

        self._id = None
        self._resource_id = None
        self._spec_code = None
        self._charge_mode = None
        self._status = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if resource_id is not None:
            self.resource_id = resource_id
        if spec_code is not None:
            self.spec_code = spec_code
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        r"""Gets the id of this AssetResourceRsp.

        **参数解释**： 实例ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The id of this AssetResourceRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AssetResourceRsp.

        **参数解释**： 实例ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param id: The id of this AssetResourceRsp.
        :type id: str
        """
        self._id = id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this AssetResourceRsp.

        **参数解释**： 资源ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The resource_id of this AssetResourceRsp.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this AssetResourceRsp.

        **参数解释**： 资源ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param resource_id: The resource_id of this AssetResourceRsp.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def spec_code(self):
        r"""Gets the spec_code of this AssetResourceRsp.

        **参数解释**： 规格信息。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The spec_code of this AssetResourceRsp.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this AssetResourceRsp.

        **参数解释**： 规格信息。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param spec_code: The spec_code of this AssetResourceRsp.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this AssetResourceRsp.

        **参数解释**： 计费类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The charge_mode of this AssetResourceRsp.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this AssetResourceRsp.

        **参数解释**： 计费类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param charge_mode: The charge_mode of this AssetResourceRsp.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def status(self):
        r"""Gets the status of this AssetResourceRsp.

        :return: The status of this AssetResourceRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.AssetResourceStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AssetResourceRsp.

        :param status: The status of this AssetResourceRsp.
        :type status: :class:`huaweicloudsdkeihealth.v1.AssetResourceStatusEnum`
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this AssetResourceRsp.

        **参数解释**： 购买时间，UTC时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The create_time of this AssetResourceRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AssetResourceRsp.

        **参数解释**： 购买时间，UTC时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param create_time: The create_time of this AssetResourceRsp.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, AssetResourceRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
