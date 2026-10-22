# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScenarioAnnotationDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scenario_type': 'str',
        'url_match': 'UrlMatchDTO',
        'request_inspection': 'RequestInspectionDTO',
        'response_inspection': 'ResponseInspectionDTO'
    }

    attribute_map = {
        'scenario_type': 'scenario_type',
        'url_match': 'url_match',
        'request_inspection': 'request_inspection',
        'response_inspection': 'response_inspection'
    }

    def __init__(self, scenario_type=None, url_match=None, request_inspection=None, response_inspection=None):
        r"""ScenarioAnnotationDTO

        The model defined in huaweicloud sdk

        :param scenario_type: 场景类型（LOGIN/REGISTER/CUSTOM）
        :type scenario_type: str
        :param url_match: 
        :type url_match: :class:`huaweicloudsdkwaf.v1.UrlMatchDTO`
        :param request_inspection: 
        :type request_inspection: :class:`huaweicloudsdkwaf.v1.RequestInspectionDTO`
        :param response_inspection: 
        :type response_inspection: :class:`huaweicloudsdkwaf.v1.ResponseInspectionDTO`
        """
        
        

        self._scenario_type = None
        self._url_match = None
        self._request_inspection = None
        self._response_inspection = None
        self.discriminator = None

        self.scenario_type = scenario_type
        self.url_match = url_match
        self.request_inspection = request_inspection
        if response_inspection is not None:
            self.response_inspection = response_inspection

    @property
    def scenario_type(self):
        r"""Gets the scenario_type of this ScenarioAnnotationDTO.

        场景类型（LOGIN/REGISTER/CUSTOM）

        :return: The scenario_type of this ScenarioAnnotationDTO.
        :rtype: str
        """
        return self._scenario_type

    @scenario_type.setter
    def scenario_type(self, scenario_type):
        r"""Sets the scenario_type of this ScenarioAnnotationDTO.

        场景类型（LOGIN/REGISTER/CUSTOM）

        :param scenario_type: The scenario_type of this ScenarioAnnotationDTO.
        :type scenario_type: str
        """
        self._scenario_type = scenario_type

    @property
    def url_match(self):
        r"""Gets the url_match of this ScenarioAnnotationDTO.

        :return: The url_match of this ScenarioAnnotationDTO.
        :rtype: :class:`huaweicloudsdkwaf.v1.UrlMatchDTO`
        """
        return self._url_match

    @url_match.setter
    def url_match(self, url_match):
        r"""Sets the url_match of this ScenarioAnnotationDTO.

        :param url_match: The url_match of this ScenarioAnnotationDTO.
        :type url_match: :class:`huaweicloudsdkwaf.v1.UrlMatchDTO`
        """
        self._url_match = url_match

    @property
    def request_inspection(self):
        r"""Gets the request_inspection of this ScenarioAnnotationDTO.

        :return: The request_inspection of this ScenarioAnnotationDTO.
        :rtype: :class:`huaweicloudsdkwaf.v1.RequestInspectionDTO`
        """
        return self._request_inspection

    @request_inspection.setter
    def request_inspection(self, request_inspection):
        r"""Sets the request_inspection of this ScenarioAnnotationDTO.

        :param request_inspection: The request_inspection of this ScenarioAnnotationDTO.
        :type request_inspection: :class:`huaweicloudsdkwaf.v1.RequestInspectionDTO`
        """
        self._request_inspection = request_inspection

    @property
    def response_inspection(self):
        r"""Gets the response_inspection of this ScenarioAnnotationDTO.

        :return: The response_inspection of this ScenarioAnnotationDTO.
        :rtype: :class:`huaweicloudsdkwaf.v1.ResponseInspectionDTO`
        """
        return self._response_inspection

    @response_inspection.setter
    def response_inspection(self, response_inspection):
        r"""Sets the response_inspection of this ScenarioAnnotationDTO.

        :param response_inspection: The response_inspection of this ScenarioAnnotationDTO.
        :type response_inspection: :class:`huaweicloudsdkwaf.v1.ResponseInspectionDTO`
        """
        self._response_inspection = response_inspection

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
        if not isinstance(other, ScenarioAnnotationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
