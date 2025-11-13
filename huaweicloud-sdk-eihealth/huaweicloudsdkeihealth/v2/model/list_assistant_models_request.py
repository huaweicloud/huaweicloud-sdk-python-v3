# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssistantModelsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vendor_id': 'str',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'vendor_id': 'vendor_id',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, vendor_id=None, sort_key=None, sort_dir=None):
        r"""ListAssistantModelsRequest

        The model defined in huaweicloud sdk

        :param vendor_id: **参数解释**： 模型供应商ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 
        :type vendor_id: str
        :param sort_key: **参数解释**： 排序规则，目前默认创建时间降序。 **约束限制**： 不涉及 **取值范围**：   * service_name：服务名称   * name：模型名称   * type：模型类型   * update_time：修改时间 **默认取值**： update_time 
        :type sort_key: str
        :param sort_dir: **参数解释**： 排序方向。 **约束限制**： 不涉及 **取值范围**： - acs：升序 - desc：降序 **默认取值**： desc 
        :type sort_dir: str
        """
        
        

        self._vendor_id = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.vendor_id = vendor_id
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def vendor_id(self):
        r"""Gets the vendor_id of this ListAssistantModelsRequest.

        **参数解释**： 模型供应商ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :return: The vendor_id of this ListAssistantModelsRequest.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        r"""Sets the vendor_id of this ListAssistantModelsRequest.

        **参数解释**： 模型供应商ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :param vendor_id: The vendor_id of this ListAssistantModelsRequest.
        :type vendor_id: str
        """
        self._vendor_id = vendor_id

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListAssistantModelsRequest.

        **参数解释**： 排序规则，目前默认创建时间降序。 **约束限制**： 不涉及 **取值范围**：   * service_name：服务名称   * name：模型名称   * type：模型类型   * update_time：修改时间 **默认取值**： update_time 

        :return: The sort_key of this ListAssistantModelsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListAssistantModelsRequest.

        **参数解释**： 排序规则，目前默认创建时间降序。 **约束限制**： 不涉及 **取值范围**：   * service_name：服务名称   * name：模型名称   * type：模型类型   * update_time：修改时间 **默认取值**： update_time 

        :param sort_key: The sort_key of this ListAssistantModelsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListAssistantModelsRequest.

        **参数解释**： 排序方向。 **约束限制**： 不涉及 **取值范围**： - acs：升序 - desc：降序 **默认取值**： desc 

        :return: The sort_dir of this ListAssistantModelsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListAssistantModelsRequest.

        **参数解释**： 排序方向。 **约束限制**： 不涉及 **取值范围**： - acs：升序 - desc：降序 **默认取值**： desc 

        :param sort_dir: The sort_dir of this ListAssistantModelsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListAssistantModelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
