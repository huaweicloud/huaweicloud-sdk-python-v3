# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowMainServiceAuthReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'main_service_id': 'str',
        'content_id': 'str',
        'consume': 'WorkflowConsume'
    }

    attribute_map = {
        'main_service_id': 'main_service_id',
        'content_id': 'content_id',
        'consume': 'consume'
    }

    def __init__(self, main_service_id=None, content_id=None, consume=None):
        r"""WorkflowMainServiceAuthReq

        The model defined in huaweicloud sdk

        :param main_service_id: 在线服务ID。
        :type main_service_id: str
        :param content_id: Gallery资产ID。
        :type content_id: str
        :param consume: 
        :type consume: :class:`huaweicloudsdkmodelarts.v1.WorkflowConsume`
        """
        
        

        self._main_service_id = None
        self._content_id = None
        self._consume = None
        self.discriminator = None

        if main_service_id is not None:
            self.main_service_id = main_service_id
        if content_id is not None:
            self.content_id = content_id
        if consume is not None:
            self.consume = consume

    @property
    def main_service_id(self):
        r"""Gets the main_service_id of this WorkflowMainServiceAuthReq.

        在线服务ID。

        :return: The main_service_id of this WorkflowMainServiceAuthReq.
        :rtype: str
        """
        return self._main_service_id

    @main_service_id.setter
    def main_service_id(self, main_service_id):
        r"""Sets the main_service_id of this WorkflowMainServiceAuthReq.

        在线服务ID。

        :param main_service_id: The main_service_id of this WorkflowMainServiceAuthReq.
        :type main_service_id: str
        """
        self._main_service_id = main_service_id

    @property
    def content_id(self):
        r"""Gets the content_id of this WorkflowMainServiceAuthReq.

        Gallery资产ID。

        :return: The content_id of this WorkflowMainServiceAuthReq.
        :rtype: str
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        r"""Sets the content_id of this WorkflowMainServiceAuthReq.

        Gallery资产ID。

        :param content_id: The content_id of this WorkflowMainServiceAuthReq.
        :type content_id: str
        """
        self._content_id = content_id

    @property
    def consume(self):
        r"""Gets the consume of this WorkflowMainServiceAuthReq.

        :return: The consume of this WorkflowMainServiceAuthReq.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.WorkflowConsume`
        """
        return self._consume

    @consume.setter
    def consume(self, consume):
        r"""Sets the consume of this WorkflowMainServiceAuthReq.

        :param consume: The consume of this WorkflowMainServiceAuthReq.
        :type consume: :class:`huaweicloudsdkmodelarts.v1.WorkflowConsume`
        """
        self._consume = consume

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
        if not isinstance(other, WorkflowMainServiceAuthReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
