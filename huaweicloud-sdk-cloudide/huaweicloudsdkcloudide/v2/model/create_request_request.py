# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRequestRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topn': 'int',
        'scenario': 'str',
        'resubmit': 'bool',
        'model_id': 'str',
        'request_type': 'str',
        'body': 'PropertiesSchema'
    }

    attribute_map = {
        'topn': 'topn',
        'scenario': 'scenario',
        'resubmit': 'resubmit',
        'model_id': 'model_id',
        'request_type': 'request_type',
        'body': 'body'
    }

    def __init__(self, topn=None, scenario=None, resubmit=None, model_id=None, request_type=None, body=None):
        """CreateRequestRequest

        The model defined in huaweicloud sdk

        :param topn: the number of samples
        :type topn: int
        :param scenario: the scenario of code content
        :type scenario: str
        :param resubmit: if &#x60;resubmit&#x60; is true, the de-duplication will be ignored
        :type resubmit: bool
        :param model_id: choose the model
        :type model_id: str
        :param request_type: An enumeration. - function - rawtext
        :type request_type: str
        :param body: Body of the CreateRequestRequest
        :type body: :class:`huaweicloudsdkcloudide.v2.PropertiesSchema`
        """
        
        

        self._topn = None
        self._scenario = None
        self._resubmit = None
        self._model_id = None
        self._request_type = None
        self._body = None
        self.discriminator = None

        if topn is not None:
            self.topn = topn
        if scenario is not None:
            self.scenario = scenario
        if resubmit is not None:
            self.resubmit = resubmit
        if model_id is not None:
            self.model_id = model_id
        if request_type is not None:
            self.request_type = request_type
        if body is not None:
            self.body = body

    @property
    def topn(self):
        """Gets the topn of this CreateRequestRequest.

        the number of samples

        :return: The topn of this CreateRequestRequest.
        :rtype: int
        """
        return self._topn

    @topn.setter
    def topn(self, topn):
        """Sets the topn of this CreateRequestRequest.

        the number of samples

        :param topn: The topn of this CreateRequestRequest.
        :type topn: int
        """
        self._topn = topn

    @property
    def scenario(self):
        """Gets the scenario of this CreateRequestRequest.

        the scenario of code content

        :return: The scenario of this CreateRequestRequest.
        :rtype: str
        """
        return self._scenario

    @scenario.setter
    def scenario(self, scenario):
        """Sets the scenario of this CreateRequestRequest.

        the scenario of code content

        :param scenario: The scenario of this CreateRequestRequest.
        :type scenario: str
        """
        self._scenario = scenario

    @property
    def resubmit(self):
        """Gets the resubmit of this CreateRequestRequest.

        if `resubmit` is true, the de-duplication will be ignored

        :return: The resubmit of this CreateRequestRequest.
        :rtype: bool
        """
        return self._resubmit

    @resubmit.setter
    def resubmit(self, resubmit):
        """Sets the resubmit of this CreateRequestRequest.

        if `resubmit` is true, the de-duplication will be ignored

        :param resubmit: The resubmit of this CreateRequestRequest.
        :type resubmit: bool
        """
        self._resubmit = resubmit

    @property
    def model_id(self):
        """Gets the model_id of this CreateRequestRequest.

        choose the model

        :return: The model_id of this CreateRequestRequest.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this CreateRequestRequest.

        choose the model

        :param model_id: The model_id of this CreateRequestRequest.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def request_type(self):
        """Gets the request_type of this CreateRequestRequest.

        An enumeration. - function - rawtext

        :return: The request_type of this CreateRequestRequest.
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """Sets the request_type of this CreateRequestRequest.

        An enumeration. - function - rawtext

        :param request_type: The request_type of this CreateRequestRequest.
        :type request_type: str
        """
        self._request_type = request_type

    @property
    def body(self):
        """Gets the body of this CreateRequestRequest.

        :return: The body of this CreateRequestRequest.
        :rtype: :class:`huaweicloudsdkcloudide.v2.PropertiesSchema`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateRequestRequest.

        :param body: The body of this CreateRequestRequest.
        :type body: :class:`huaweicloudsdkcloudide.v2.PropertiesSchema`
        """
        self._body = body

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
        if not isinstance(other, CreateRequestRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
