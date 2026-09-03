# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartTestsuiteUsingRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_id': 'str',
        'suite_id': 'str',
        'body': 'TaskActionParamsV5'
    }

    attribute_map = {
        'service_id': 'service_id',
        'suite_id': 'suite_id',
        'body': 'body'
    }

    def __init__(self, service_id=None, suite_id=None, body=None):
        r"""StartTestsuiteUsingRequest

        The model defined in huaweicloud sdk

        :param service_id: 服务id
        :type service_id: str
        :param suite_id: 任务id
        :type suite_id: str
        :param body: Body of the StartTestsuiteUsingRequest
        :type body: :class:`huaweicloudsdkcloudtest.v1.TaskActionParamsV5`
        """
        
        

        self._service_id = None
        self._suite_id = None
        self._body = None
        self.discriminator = None

        self.service_id = service_id
        self.suite_id = suite_id
        if body is not None:
            self.body = body

    @property
    def service_id(self):
        r"""Gets the service_id of this StartTestsuiteUsingRequest.

        服务id

        :return: The service_id of this StartTestsuiteUsingRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this StartTestsuiteUsingRequest.

        服务id

        :param service_id: The service_id of this StartTestsuiteUsingRequest.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def suite_id(self):
        r"""Gets the suite_id of this StartTestsuiteUsingRequest.

        任务id

        :return: The suite_id of this StartTestsuiteUsingRequest.
        :rtype: str
        """
        return self._suite_id

    @suite_id.setter
    def suite_id(self, suite_id):
        r"""Sets the suite_id of this StartTestsuiteUsingRequest.

        任务id

        :param suite_id: The suite_id of this StartTestsuiteUsingRequest.
        :type suite_id: str
        """
        self._suite_id = suite_id

    @property
    def body(self):
        r"""Gets the body of this StartTestsuiteUsingRequest.

        :return: The body of this StartTestsuiteUsingRequest.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TaskActionParamsV5`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this StartTestsuiteUsingRequest.

        :param body: The body of this StartTestsuiteUsingRequest.
        :type body: :class:`huaweicloudsdkcloudtest.v1.TaskActionParamsV5`
        """
        self._body = body

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
        if not isinstance(other, StartTestsuiteUsingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
