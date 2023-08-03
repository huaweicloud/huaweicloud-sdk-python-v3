# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmnTargetDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'urn': 'str',
        'agency_name': 'str',
        'subject_transform': 'SmnTargetDetailSubjectTransform'
    }

    attribute_map = {
        'urn': 'urn',
        'agency_name': 'agency_name',
        'subject_transform': 'subject_transform'
    }

    def __init__(self, urn=None, agency_name=None, subject_transform=None):
        """SmnTargetDetail

        The model defined in huaweicloud sdk

        :param urn: 主题urn
        :type urn: str
        :param agency_name: 委托名称
        :type agency_name: str
        :param subject_transform: 
        :type subject_transform: :class:`huaweicloudsdkeg.v1.SmnTargetDetailSubjectTransform`
        """
        
        

        self._urn = None
        self._agency_name = None
        self._subject_transform = None
        self.discriminator = None

        self.urn = urn
        self.agency_name = agency_name
        if subject_transform is not None:
            self.subject_transform = subject_transform

    @property
    def urn(self):
        """Gets the urn of this SmnTargetDetail.

        主题urn

        :return: The urn of this SmnTargetDetail.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this SmnTargetDetail.

        主题urn

        :param urn: The urn of this SmnTargetDetail.
        :type urn: str
        """
        self._urn = urn

    @property
    def agency_name(self):
        """Gets the agency_name of this SmnTargetDetail.

        委托名称

        :return: The agency_name of this SmnTargetDetail.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        """Sets the agency_name of this SmnTargetDetail.

        委托名称

        :param agency_name: The agency_name of this SmnTargetDetail.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def subject_transform(self):
        """Gets the subject_transform of this SmnTargetDetail.

        :return: The subject_transform of this SmnTargetDetail.
        :rtype: :class:`huaweicloudsdkeg.v1.SmnTargetDetailSubjectTransform`
        """
        return self._subject_transform

    @subject_transform.setter
    def subject_transform(self, subject_transform):
        """Sets the subject_transform of this SmnTargetDetail.

        :param subject_transform: The subject_transform of this SmnTargetDetail.
        :type subject_transform: :class:`huaweicloudsdkeg.v1.SmnTargetDetailSubjectTransform`
        """
        self._subject_transform = subject_transform

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
        if not isinstance(other, SmnTargetDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
