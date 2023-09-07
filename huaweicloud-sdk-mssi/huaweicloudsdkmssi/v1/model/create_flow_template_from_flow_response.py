# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFlowTemplateFromFlowResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'apig_url': 'str',
        'flow_id': 'str',
        'steps': 'list[object]',
        'webhook': 'str'
    }

    attribute_map = {
        'apig_url': 'apig_url',
        'flow_id': 'flow_id',
        'steps': 'steps',
        'webhook': 'webhook'
    }

    def __init__(self, apig_url=None, flow_id=None, steps=None, webhook=None):
        """CreateFlowTemplateFromFlowResponse

        The model defined in huaweicloud sdk

        :param apig_url: api流注册到apig的url
        :type apig_url: str
        :param flow_id: ID
        :type flow_id: str
        :param steps: 函数连接器对应functionId
        :type steps: list[object]
        :param webhook: webhook触发url的ID
        :type webhook: str
        """
        
        super(CreateFlowTemplateFromFlowResponse, self).__init__()

        self._apig_url = None
        self._flow_id = None
        self._steps = None
        self._webhook = None
        self.discriminator = None

        if apig_url is not None:
            self.apig_url = apig_url
        if flow_id is not None:
            self.flow_id = flow_id
        if steps is not None:
            self.steps = steps
        if webhook is not None:
            self.webhook = webhook

    @property
    def apig_url(self):
        """Gets the apig_url of this CreateFlowTemplateFromFlowResponse.

        api流注册到apig的url

        :return: The apig_url of this CreateFlowTemplateFromFlowResponse.
        :rtype: str
        """
        return self._apig_url

    @apig_url.setter
    def apig_url(self, apig_url):
        """Sets the apig_url of this CreateFlowTemplateFromFlowResponse.

        api流注册到apig的url

        :param apig_url: The apig_url of this CreateFlowTemplateFromFlowResponse.
        :type apig_url: str
        """
        self._apig_url = apig_url

    @property
    def flow_id(self):
        """Gets the flow_id of this CreateFlowTemplateFromFlowResponse.

        ID

        :return: The flow_id of this CreateFlowTemplateFromFlowResponse.
        :rtype: str
        """
        return self._flow_id

    @flow_id.setter
    def flow_id(self, flow_id):
        """Sets the flow_id of this CreateFlowTemplateFromFlowResponse.

        ID

        :param flow_id: The flow_id of this CreateFlowTemplateFromFlowResponse.
        :type flow_id: str
        """
        self._flow_id = flow_id

    @property
    def steps(self):
        """Gets the steps of this CreateFlowTemplateFromFlowResponse.

        函数连接器对应functionId

        :return: The steps of this CreateFlowTemplateFromFlowResponse.
        :rtype: list[object]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this CreateFlowTemplateFromFlowResponse.

        函数连接器对应functionId

        :param steps: The steps of this CreateFlowTemplateFromFlowResponse.
        :type steps: list[object]
        """
        self._steps = steps

    @property
    def webhook(self):
        """Gets the webhook of this CreateFlowTemplateFromFlowResponse.

        webhook触发url的ID

        :return: The webhook of this CreateFlowTemplateFromFlowResponse.
        :rtype: str
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this CreateFlowTemplateFromFlowResponse.

        webhook触发url的ID

        :param webhook: The webhook of this CreateFlowTemplateFromFlowResponse.
        :type webhook: str
        """
        self._webhook = webhook

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
        if not isinstance(other, CreateFlowTemplateFromFlowResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
