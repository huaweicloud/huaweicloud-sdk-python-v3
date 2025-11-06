# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeContainerStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'container_id': 'str',
        'container_name': 'str',
        'success': 'bool',
        'new_status': 'str'
    }

    attribute_map = {
        'container_id': 'container_id',
        'container_name': 'container_name',
        'success': 'success',
        'new_status': 'new_status'
    }

    def __init__(self, container_id=None, container_name=None, success=None, new_status=None):
        r"""ChangeContainerStatusResponse

        The model defined in huaweicloud sdk

        :param container_id: **参数解释**: 容器ID **取值范围**: 字符长度1-256位 
        :type container_id: str
        :param container_name: **参数解释**： 容器名称 **取值范围**： 字符长度1-256位 
        :type container_name: str
        :param success: **参数解释**: 是否成功 **取值范围**: - true：是。 - false：否。 
        :type success: bool
        :param new_status: **参数解释**： 状态 **取值范围**： - Running：运行中。 - Terminated：终止。 - Waiting：等待。 - Isolated：已隔离。 
        :type new_status: str
        """
        
        super().__init__()

        self._container_id = None
        self._container_name = None
        self._success = None
        self._new_status = None
        self.discriminator = None

        if container_id is not None:
            self.container_id = container_id
        if container_name is not None:
            self.container_name = container_name
        if success is not None:
            self.success = success
        if new_status is not None:
            self.new_status = new_status

    @property
    def container_id(self):
        r"""Gets the container_id of this ChangeContainerStatusResponse.

        **参数解释**: 容器ID **取值范围**: 字符长度1-256位 

        :return: The container_id of this ChangeContainerStatusResponse.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this ChangeContainerStatusResponse.

        **参数解释**: 容器ID **取值范围**: 字符长度1-256位 

        :param container_id: The container_id of this ChangeContainerStatusResponse.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        r"""Gets the container_name of this ChangeContainerStatusResponse.

        **参数解释**： 容器名称 **取值范围**： 字符长度1-256位 

        :return: The container_name of this ChangeContainerStatusResponse.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ChangeContainerStatusResponse.

        **参数解释**： 容器名称 **取值范围**： 字符长度1-256位 

        :param container_name: The container_name of this ChangeContainerStatusResponse.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def success(self):
        r"""Gets the success of this ChangeContainerStatusResponse.

        **参数解释**: 是否成功 **取值范围**: - true：是。 - false：否。 

        :return: The success of this ChangeContainerStatusResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ChangeContainerStatusResponse.

        **参数解释**: 是否成功 **取值范围**: - true：是。 - false：否。 

        :param success: The success of this ChangeContainerStatusResponse.
        :type success: bool
        """
        self._success = success

    @property
    def new_status(self):
        r"""Gets the new_status of this ChangeContainerStatusResponse.

        **参数解释**： 状态 **取值范围**： - Running：运行中。 - Terminated：终止。 - Waiting：等待。 - Isolated：已隔离。 

        :return: The new_status of this ChangeContainerStatusResponse.
        :rtype: str
        """
        return self._new_status

    @new_status.setter
    def new_status(self, new_status):
        r"""Sets the new_status of this ChangeContainerStatusResponse.

        **参数解释**： 状态 **取值范围**： - Running：运行中。 - Terminated：终止。 - Waiting：等待。 - Isolated：已隔离。 

        :param new_status: The new_status of this ChangeContainerStatusResponse.
        :type new_status: str
        """
        self._new_status = new_status

    def to_dict(self):
        import warnings
        warnings.warn("ChangeContainerStatusResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ChangeContainerStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
