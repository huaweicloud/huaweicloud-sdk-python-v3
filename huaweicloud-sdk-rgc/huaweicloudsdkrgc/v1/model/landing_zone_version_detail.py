# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LandingZoneVersionDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'release_date': 'str',
        'release_notes': 'str'
    }

    attribute_map = {
        'version': 'version',
        'release_date': 'release_date',
        'release_notes': 'release_notes'
    }

    def __init__(self, version=None, release_date=None, release_notes=None):
        r"""LandingZoneVersionDetail

        The model defined in huaweicloud sdk

        :param version: Landing Zone版本。
        :type version: str
        :param release_date: Landing Zone版本发布时间。
        :type release_date: str
        :param release_notes: Landing Zone版本发布说明。
        :type release_notes: str
        """
        
        

        self._version = None
        self._release_date = None
        self._release_notes = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if release_date is not None:
            self.release_date = release_date
        if release_notes is not None:
            self.release_notes = release_notes

    @property
    def version(self):
        r"""Gets the version of this LandingZoneVersionDetail.

        Landing Zone版本。

        :return: The version of this LandingZoneVersionDetail.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this LandingZoneVersionDetail.

        Landing Zone版本。

        :param version: The version of this LandingZoneVersionDetail.
        :type version: str
        """
        self._version = version

    @property
    def release_date(self):
        r"""Gets the release_date of this LandingZoneVersionDetail.

        Landing Zone版本发布时间。

        :return: The release_date of this LandingZoneVersionDetail.
        :rtype: str
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        r"""Sets the release_date of this LandingZoneVersionDetail.

        Landing Zone版本发布时间。

        :param release_date: The release_date of this LandingZoneVersionDetail.
        :type release_date: str
        """
        self._release_date = release_date

    @property
    def release_notes(self):
        r"""Gets the release_notes of this LandingZoneVersionDetail.

        Landing Zone版本发布说明。

        :return: The release_notes of this LandingZoneVersionDetail.
        :rtype: str
        """
        return self._release_notes

    @release_notes.setter
    def release_notes(self, release_notes):
        r"""Sets the release_notes of this LandingZoneVersionDetail.

        Landing Zone版本发布说明。

        :param release_notes: The release_notes of this LandingZoneVersionDetail.
        :type release_notes: str
        """
        self._release_notes = release_notes

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
        if not isinstance(other, LandingZoneVersionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
