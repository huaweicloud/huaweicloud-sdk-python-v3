# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIpdProjectListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'search': 'str',
        'model': 'str'
    }

    attribute_map = {
        'search': 'search',
        'model': 'model'
    }

    def __init__(self, search=None, model=None):
        r"""ShowIpdProjectListRequest

        The model defined in huaweicloud sdk

        :param search: **参数解释**： 项目名称搜索关键字。 **约束限制**： 最大256个字符。 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type search: str
        :param model: **参数解释**： IPD项目模型id。 **约束限制**： 不涉及 **取值范围**： 10001（系统设备类） 10002（独立软件类） 10003（云服务类型） **默认取值**： 不涉及
        :type model: str
        """
        
        

        self._search = None
        self._model = None
        self.discriminator = None

        if search is not None:
            self.search = search
        if model is not None:
            self.model = model

    @property
    def search(self):
        r"""Gets the search of this ShowIpdProjectListRequest.

        **参数解释**： 项目名称搜索关键字。 **约束限制**： 最大256个字符。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The search of this ShowIpdProjectListRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ShowIpdProjectListRequest.

        **参数解释**： 项目名称搜索关键字。 **约束限制**： 最大256个字符。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param search: The search of this ShowIpdProjectListRequest.
        :type search: str
        """
        self._search = search

    @property
    def model(self):
        r"""Gets the model of this ShowIpdProjectListRequest.

        **参数解释**： IPD项目模型id。 **约束限制**： 不涉及 **取值范围**： 10001（系统设备类） 10002（独立软件类） 10003（云服务类型） **默认取值**： 不涉及

        :return: The model of this ShowIpdProjectListRequest.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this ShowIpdProjectListRequest.

        **参数解释**： IPD项目模型id。 **约束限制**： 不涉及 **取值范围**： 10001（系统设备类） 10002（独立软件类） 10003（云服务类型） **默认取值**： 不涉及

        :param model: The model of this ShowIpdProjectListRequest.
        :type model: str
        """
        self._model = model

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
        if not isinstance(other, ShowIpdProjectListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
