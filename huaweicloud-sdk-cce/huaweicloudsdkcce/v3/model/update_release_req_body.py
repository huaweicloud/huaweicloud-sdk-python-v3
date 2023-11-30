# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateReleaseReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'chart_id': 'str',
        'action': 'str',
        'parameters': 'ReleaseReqBodyParams',
        'values': 'CreateReleaseReqBodyValues'
    }

    attribute_map = {
        'chart_id': 'chart_id',
        'action': 'action',
        'parameters': 'parameters',
        'values': 'values'
    }

    def __init__(self, chart_id=None, action=None, parameters=None, values=None):
        """UpdateReleaseReqBody

        The model defined in huaweicloud sdk

        :param chart_id: 模板ID
        :type chart_id: str
        :param action: 更新操作，升级为upgrade，回退为rollback
        :type action: str
        :param parameters: 
        :type parameters: :class:`huaweicloudsdkcce.v3.ReleaseReqBodyParams`
        :param values: 
        :type values: :class:`huaweicloudsdkcce.v3.CreateReleaseReqBodyValues`
        """
        
        

        self._chart_id = None
        self._action = None
        self._parameters = None
        self._values = None
        self.discriminator = None

        self.chart_id = chart_id
        self.action = action
        self.parameters = parameters
        self.values = values

    @property
    def chart_id(self):
        """Gets the chart_id of this UpdateReleaseReqBody.

        模板ID

        :return: The chart_id of this UpdateReleaseReqBody.
        :rtype: str
        """
        return self._chart_id

    @chart_id.setter
    def chart_id(self, chart_id):
        """Sets the chart_id of this UpdateReleaseReqBody.

        模板ID

        :param chart_id: The chart_id of this UpdateReleaseReqBody.
        :type chart_id: str
        """
        self._chart_id = chart_id

    @property
    def action(self):
        """Gets the action of this UpdateReleaseReqBody.

        更新操作，升级为upgrade，回退为rollback

        :return: The action of this UpdateReleaseReqBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this UpdateReleaseReqBody.

        更新操作，升级为upgrade，回退为rollback

        :param action: The action of this UpdateReleaseReqBody.
        :type action: str
        """
        self._action = action

    @property
    def parameters(self):
        """Gets the parameters of this UpdateReleaseReqBody.

        :return: The parameters of this UpdateReleaseReqBody.
        :rtype: :class:`huaweicloudsdkcce.v3.ReleaseReqBodyParams`
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this UpdateReleaseReqBody.

        :param parameters: The parameters of this UpdateReleaseReqBody.
        :type parameters: :class:`huaweicloudsdkcce.v3.ReleaseReqBodyParams`
        """
        self._parameters = parameters

    @property
    def values(self):
        """Gets the values of this UpdateReleaseReqBody.

        :return: The values of this UpdateReleaseReqBody.
        :rtype: :class:`huaweicloudsdkcce.v3.CreateReleaseReqBodyValues`
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this UpdateReleaseReqBody.

        :param values: The values of this UpdateReleaseReqBody.
        :type values: :class:`huaweicloudsdkcce.v3.CreateReleaseReqBodyValues`
        """
        self._values = values

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
        if not isinstance(other, UpdateReleaseReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
