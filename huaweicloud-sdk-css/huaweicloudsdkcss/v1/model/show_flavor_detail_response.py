# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFlavorDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'str_id': 'str',
        'name': 'str',
        'cond_operation_status': 'str',
        'cond_operation_az': 'str',
        'flavor_detail': 'list[ShowFlavorDetailRspFlavorDetail]'
    }

    attribute_map = {
        'str_id': 'str_id',
        'name': 'name',
        'cond_operation_status': 'condOperationStatus',
        'cond_operation_az': 'condOperationAz',
        'flavor_detail': 'flavor_detail'
    }

    def __init__(self, str_id=None, name=None, cond_operation_status=None, cond_operation_az=None, flavor_detail=None):
        r"""ShowFlavorDetailResponse

        The model defined in huaweicloud sdk

        :param str_id: **参数解释**： 规格id。 **取值范围**： 不涉及
        :type str_id: str
        :param name: **参数解释**： 规格名称。 **取值范围**： 不涉及
        :type name: str
        :param cond_operation_status: **参数解释**： 此参数是Region级配置，某个AZ没有在condOperationAz参数中配置时默认使用此参数的取值。 **取值范围**：   - normal：正常商用。   - sellout：售罄。
        :type cond_operation_status: str
        :param cond_operation_az: **参数解释**： 此参数是AZ级配置，某个AZ没有在此参数中配置时默认使用condOperationAz参数的取值。此参数的配置格式“az(xx)”。()内为某个AZ的flavor状态，()内必须要填有状态，不填为无效配置。状态的取值范围与condOperationStatus参数相同。 **取值范围**： 不涉及
        :type cond_operation_az: str
        :param flavor_detail: **参数解释**： 规格属性信息。 **取值范围**： 不涉及
        :type flavor_detail: list[:class:`huaweicloudsdkcss.v1.ShowFlavorDetailRspFlavorDetail`]
        """
        
        super().__init__()

        self._str_id = None
        self._name = None
        self._cond_operation_status = None
        self._cond_operation_az = None
        self._flavor_detail = None
        self.discriminator = None

        if str_id is not None:
            self.str_id = str_id
        if name is not None:
            self.name = name
        if cond_operation_status is not None:
            self.cond_operation_status = cond_operation_status
        if cond_operation_az is not None:
            self.cond_operation_az = cond_operation_az
        if flavor_detail is not None:
            self.flavor_detail = flavor_detail

    @property
    def str_id(self):
        r"""Gets the str_id of this ShowFlavorDetailResponse.

        **参数解释**： 规格id。 **取值范围**： 不涉及

        :return: The str_id of this ShowFlavorDetailResponse.
        :rtype: str
        """
        return self._str_id

    @str_id.setter
    def str_id(self, str_id):
        r"""Sets the str_id of this ShowFlavorDetailResponse.

        **参数解释**： 规格id。 **取值范围**： 不涉及

        :param str_id: The str_id of this ShowFlavorDetailResponse.
        :type str_id: str
        """
        self._str_id = str_id

    @property
    def name(self):
        r"""Gets the name of this ShowFlavorDetailResponse.

        **参数解释**： 规格名称。 **取值范围**： 不涉及

        :return: The name of this ShowFlavorDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowFlavorDetailResponse.

        **参数解释**： 规格名称。 **取值范围**： 不涉及

        :param name: The name of this ShowFlavorDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def cond_operation_status(self):
        r"""Gets the cond_operation_status of this ShowFlavorDetailResponse.

        **参数解释**： 此参数是Region级配置，某个AZ没有在condOperationAz参数中配置时默认使用此参数的取值。 **取值范围**：   - normal：正常商用。   - sellout：售罄。

        :return: The cond_operation_status of this ShowFlavorDetailResponse.
        :rtype: str
        """
        return self._cond_operation_status

    @cond_operation_status.setter
    def cond_operation_status(self, cond_operation_status):
        r"""Sets the cond_operation_status of this ShowFlavorDetailResponse.

        **参数解释**： 此参数是Region级配置，某个AZ没有在condOperationAz参数中配置时默认使用此参数的取值。 **取值范围**：   - normal：正常商用。   - sellout：售罄。

        :param cond_operation_status: The cond_operation_status of this ShowFlavorDetailResponse.
        :type cond_operation_status: str
        """
        self._cond_operation_status = cond_operation_status

    @property
    def cond_operation_az(self):
        r"""Gets the cond_operation_az of this ShowFlavorDetailResponse.

        **参数解释**： 此参数是AZ级配置，某个AZ没有在此参数中配置时默认使用condOperationAz参数的取值。此参数的配置格式“az(xx)”。()内为某个AZ的flavor状态，()内必须要填有状态，不填为无效配置。状态的取值范围与condOperationStatus参数相同。 **取值范围**： 不涉及

        :return: The cond_operation_az of this ShowFlavorDetailResponse.
        :rtype: str
        """
        return self._cond_operation_az

    @cond_operation_az.setter
    def cond_operation_az(self, cond_operation_az):
        r"""Sets the cond_operation_az of this ShowFlavorDetailResponse.

        **参数解释**： 此参数是AZ级配置，某个AZ没有在此参数中配置时默认使用condOperationAz参数的取值。此参数的配置格式“az(xx)”。()内为某个AZ的flavor状态，()内必须要填有状态，不填为无效配置。状态的取值范围与condOperationStatus参数相同。 **取值范围**： 不涉及

        :param cond_operation_az: The cond_operation_az of this ShowFlavorDetailResponse.
        :type cond_operation_az: str
        """
        self._cond_operation_az = cond_operation_az

    @property
    def flavor_detail(self):
        r"""Gets the flavor_detail of this ShowFlavorDetailResponse.

        **参数解释**： 规格属性信息。 **取值范围**： 不涉及

        :return: The flavor_detail of this ShowFlavorDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.ShowFlavorDetailRspFlavorDetail`]
        """
        return self._flavor_detail

    @flavor_detail.setter
    def flavor_detail(self, flavor_detail):
        r"""Sets the flavor_detail of this ShowFlavorDetailResponse.

        **参数解释**： 规格属性信息。 **取值范围**： 不涉及

        :param flavor_detail: The flavor_detail of this ShowFlavorDetailResponse.
        :type flavor_detail: list[:class:`huaweicloudsdkcss.v1.ShowFlavorDetailRspFlavorDetail`]
        """
        self._flavor_detail = flavor_detail

    def to_dict(self):
        import warnings
        warnings.warn("ShowFlavorDetailResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowFlavorDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
