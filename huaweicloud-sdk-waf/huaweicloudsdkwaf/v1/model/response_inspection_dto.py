# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponseInspectionDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component_type': 'str',
        'json_path': 'str',
        'success': 'list[str]',
        'fail': 'list[str]'
    }

    attribute_map = {
        'component_type': 'component_type',
        'json_path': 'json_path',
        'success': 'success',
        'fail': 'fail'
    }

    def __init__(self, component_type=None, json_path=None, success=None, fail=None):
        r"""ResponseInspectionDTO

        The model defined in huaweicloud sdk

        :param component_type: 响应中表明成功或失败的组件（JSON/STATUS_CODE）
        :type component_type: str
        :param json_path: JSON 路径（JSON时必选）
        :type json_path: str
        :param success: 成功响应判定（可选）
        :type success: list[str]
        :param fail: 失败响应判定（可选）
        :type fail: list[str]
        """
        
        

        self._component_type = None
        self._json_path = None
        self._success = None
        self._fail = None
        self.discriminator = None

        self.component_type = component_type
        if json_path is not None:
            self.json_path = json_path
        if success is not None:
            self.success = success
        if fail is not None:
            self.fail = fail

    @property
    def component_type(self):
        r"""Gets the component_type of this ResponseInspectionDTO.

        响应中表明成功或失败的组件（JSON/STATUS_CODE）

        :return: The component_type of this ResponseInspectionDTO.
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        r"""Sets the component_type of this ResponseInspectionDTO.

        响应中表明成功或失败的组件（JSON/STATUS_CODE）

        :param component_type: The component_type of this ResponseInspectionDTO.
        :type component_type: str
        """
        self._component_type = component_type

    @property
    def json_path(self):
        r"""Gets the json_path of this ResponseInspectionDTO.

        JSON 路径（JSON时必选）

        :return: The json_path of this ResponseInspectionDTO.
        :rtype: str
        """
        return self._json_path

    @json_path.setter
    def json_path(self, json_path):
        r"""Sets the json_path of this ResponseInspectionDTO.

        JSON 路径（JSON时必选）

        :param json_path: The json_path of this ResponseInspectionDTO.
        :type json_path: str
        """
        self._json_path = json_path

    @property
    def success(self):
        r"""Gets the success of this ResponseInspectionDTO.

        成功响应判定（可选）

        :return: The success of this ResponseInspectionDTO.
        :rtype: list[str]
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ResponseInspectionDTO.

        成功响应判定（可选）

        :param success: The success of this ResponseInspectionDTO.
        :type success: list[str]
        """
        self._success = success

    @property
    def fail(self):
        r"""Gets the fail of this ResponseInspectionDTO.

        失败响应判定（可选）

        :return: The fail of this ResponseInspectionDTO.
        :rtype: list[str]
        """
        return self._fail

    @fail.setter
    def fail(self, fail):
        r"""Sets the fail of this ResponseInspectionDTO.

        失败响应判定（可选）

        :param fail: The fail of this ResponseInspectionDTO.
        :type fail: list[str]
        """
        self._fail = fail

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
        if not isinstance(other, ResponseInspectionDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
