# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageVulCveInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cve_id': 'str',
        'cvss_score': 'float',
        'publish_time': 'int',
        'description': 'str'
    }

    attribute_map = {
        'cve_id': 'cve_id',
        'cvss_score': 'cvss_score',
        'publish_time': 'publish_time',
        'description': 'description'
    }

    def __init__(self, cve_id=None, cvss_score=None, publish_time=None, description=None):
        """ImageVulCveInfo

        The model defined in huaweicloud sdk

        :param cve_id: cve id
        :type cve_id: str
        :param cvss_score: CVSS分数
        :type cvss_score: float
        :param publish_time: 公布时间
        :type publish_time: int
        :param description: cve描述
        :type description: str
        """
        
        

        self._cve_id = None
        self._cvss_score = None
        self._publish_time = None
        self._description = None
        self.discriminator = None

        if cve_id is not None:
            self.cve_id = cve_id
        if cvss_score is not None:
            self.cvss_score = cvss_score
        if publish_time is not None:
            self.publish_time = publish_time
        if description is not None:
            self.description = description

    @property
    def cve_id(self):
        """Gets the cve_id of this ImageVulCveInfo.

        cve id

        :return: The cve_id of this ImageVulCveInfo.
        :rtype: str
        """
        return self._cve_id

    @cve_id.setter
    def cve_id(self, cve_id):
        """Sets the cve_id of this ImageVulCveInfo.

        cve id

        :param cve_id: The cve_id of this ImageVulCveInfo.
        :type cve_id: str
        """
        self._cve_id = cve_id

    @property
    def cvss_score(self):
        """Gets the cvss_score of this ImageVulCveInfo.

        CVSS分数

        :return: The cvss_score of this ImageVulCveInfo.
        :rtype: float
        """
        return self._cvss_score

    @cvss_score.setter
    def cvss_score(self, cvss_score):
        """Sets the cvss_score of this ImageVulCveInfo.

        CVSS分数

        :param cvss_score: The cvss_score of this ImageVulCveInfo.
        :type cvss_score: float
        """
        self._cvss_score = cvss_score

    @property
    def publish_time(self):
        """Gets the publish_time of this ImageVulCveInfo.

        公布时间

        :return: The publish_time of this ImageVulCveInfo.
        :rtype: int
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this ImageVulCveInfo.

        公布时间

        :param publish_time: The publish_time of this ImageVulCveInfo.
        :type publish_time: int
        """
        self._publish_time = publish_time

    @property
    def description(self):
        """Gets the description of this ImageVulCveInfo.

        cve描述

        :return: The description of this ImageVulCveInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ImageVulCveInfo.

        cve描述

        :param description: The description of this ImageVulCveInfo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ImageVulCveInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
