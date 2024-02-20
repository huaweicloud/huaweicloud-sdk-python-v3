# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Configuration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iam_agency': 'IAMAgency',
        'obs_bucket': 'OBSBucket'
    }

    attribute_map = {
        'iam_agency': 'iam_agency',
        'obs_bucket': 'obs_bucket'
    }

    def __init__(self, iam_agency=None, obs_bucket=None):
        """Configuration

        The model defined in huaweicloud sdk

        :param iam_agency: 
        :type iam_agency: :class:`huaweicloudsdkiamaccessanalyzer.v1.IAMAgency`
        :param obs_bucket: 
        :type obs_bucket: :class:`huaweicloudsdkiamaccessanalyzer.v1.OBSBucket`
        """
        
        

        self._iam_agency = None
        self._obs_bucket = None
        self.discriminator = None

        if iam_agency is not None:
            self.iam_agency = iam_agency
        if obs_bucket is not None:
            self.obs_bucket = obs_bucket

    @property
    def iam_agency(self):
        """Gets the iam_agency of this Configuration.

        :return: The iam_agency of this Configuration.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.IAMAgency`
        """
        return self._iam_agency

    @iam_agency.setter
    def iam_agency(self, iam_agency):
        """Sets the iam_agency of this Configuration.

        :param iam_agency: The iam_agency of this Configuration.
        :type iam_agency: :class:`huaweicloudsdkiamaccessanalyzer.v1.IAMAgency`
        """
        self._iam_agency = iam_agency

    @property
    def obs_bucket(self):
        """Gets the obs_bucket of this Configuration.

        :return: The obs_bucket of this Configuration.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.OBSBucket`
        """
        return self._obs_bucket

    @obs_bucket.setter
    def obs_bucket(self, obs_bucket):
        """Sets the obs_bucket of this Configuration.

        :param obs_bucket: The obs_bucket of this Configuration.
        :type obs_bucket: :class:`huaweicloudsdkiamaccessanalyzer.v1.OBSBucket`
        """
        self._obs_bucket = obs_bucket

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
        if not isinstance(other, Configuration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
