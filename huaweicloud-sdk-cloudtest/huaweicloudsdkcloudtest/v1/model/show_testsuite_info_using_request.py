# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTestsuiteInfoUsingRequest:

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
        'plan_id': 'str'
    }

    attribute_map = {
        'service_id': 'service_id',
        'suite_id': 'suite_id',
        'plan_id': 'planId'
    }

    def __init__(self, service_id=None, suite_id=None, plan_id=None):
        r"""ShowTestsuiteInfoUsingRequest

        The model defined in huaweicloud sdk

        :param service_id: 服务id
        :type service_id: str
        :param suite_id: 任务id
        :type suite_id: str
        :param plan_id: 测试计划Id
        :type plan_id: str
        """
        
        

        self._service_id = None
        self._suite_id = None
        self._plan_id = None
        self.discriminator = None

        self.service_id = service_id
        self.suite_id = suite_id
        if plan_id is not None:
            self.plan_id = plan_id

    @property
    def service_id(self):
        r"""Gets the service_id of this ShowTestsuiteInfoUsingRequest.

        服务id

        :return: The service_id of this ShowTestsuiteInfoUsingRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this ShowTestsuiteInfoUsingRequest.

        服务id

        :param service_id: The service_id of this ShowTestsuiteInfoUsingRequest.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def suite_id(self):
        r"""Gets the suite_id of this ShowTestsuiteInfoUsingRequest.

        任务id

        :return: The suite_id of this ShowTestsuiteInfoUsingRequest.
        :rtype: str
        """
        return self._suite_id

    @suite_id.setter
    def suite_id(self, suite_id):
        r"""Sets the suite_id of this ShowTestsuiteInfoUsingRequest.

        任务id

        :param suite_id: The suite_id of this ShowTestsuiteInfoUsingRequest.
        :type suite_id: str
        """
        self._suite_id = suite_id

    @property
    def plan_id(self):
        r"""Gets the plan_id of this ShowTestsuiteInfoUsingRequest.

        测试计划Id

        :return: The plan_id of this ShowTestsuiteInfoUsingRequest.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        r"""Sets the plan_id of this ShowTestsuiteInfoUsingRequest.

        测试计划Id

        :param plan_id: The plan_id of this ShowTestsuiteInfoUsingRequest.
        :type plan_id: str
        """
        self._plan_id = plan_id

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
        if not isinstance(other, ShowTestsuiteInfoUsingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
