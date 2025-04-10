# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExitEntryPermitEndorsementInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endorsement_type': 'str',
        'valid_round_trips': 'str',
        'endorsement_valid_period': 'str',
        'remark': 'str',
        'issue_info': 'str'
    }

    attribute_map = {
        'endorsement_type': 'endorsement_type',
        'valid_round_trips': 'valid_round_trips',
        'endorsement_valid_period': 'endorsement_valid_period',
        'remark': 'remark',
        'issue_info': 'issue_info'
    }

    def __init__(self, endorsement_type=None, valid_round_trips=None, endorsement_valid_period=None, remark=None, issue_info=None):
        r"""ExitEntryPermitEndorsementInfo

        The model defined in huaweicloud sdk

        :param endorsement_type: 签注种类。 
        :type endorsement_type: str
        :param valid_round_trips: 签注往返有效次数。 
        :type valid_round_trips: str
        :param endorsement_valid_period: 签注有效期。 
        :type endorsement_valid_period: str
        :param remark: 签注备注。 
        :type remark: str
        :param issue_info: 签注签发信息。 
        :type issue_info: str
        """
        
        

        self._endorsement_type = None
        self._valid_round_trips = None
        self._endorsement_valid_period = None
        self._remark = None
        self._issue_info = None
        self.discriminator = None

        if endorsement_type is not None:
            self.endorsement_type = endorsement_type
        if valid_round_trips is not None:
            self.valid_round_trips = valid_round_trips
        if endorsement_valid_period is not None:
            self.endorsement_valid_period = endorsement_valid_period
        if remark is not None:
            self.remark = remark
        if issue_info is not None:
            self.issue_info = issue_info

    @property
    def endorsement_type(self):
        r"""Gets the endorsement_type of this ExitEntryPermitEndorsementInfo.

        签注种类。 

        :return: The endorsement_type of this ExitEntryPermitEndorsementInfo.
        :rtype: str
        """
        return self._endorsement_type

    @endorsement_type.setter
    def endorsement_type(self, endorsement_type):
        r"""Sets the endorsement_type of this ExitEntryPermitEndorsementInfo.

        签注种类。 

        :param endorsement_type: The endorsement_type of this ExitEntryPermitEndorsementInfo.
        :type endorsement_type: str
        """
        self._endorsement_type = endorsement_type

    @property
    def valid_round_trips(self):
        r"""Gets the valid_round_trips of this ExitEntryPermitEndorsementInfo.

        签注往返有效次数。 

        :return: The valid_round_trips of this ExitEntryPermitEndorsementInfo.
        :rtype: str
        """
        return self._valid_round_trips

    @valid_round_trips.setter
    def valid_round_trips(self, valid_round_trips):
        r"""Sets the valid_round_trips of this ExitEntryPermitEndorsementInfo.

        签注往返有效次数。 

        :param valid_round_trips: The valid_round_trips of this ExitEntryPermitEndorsementInfo.
        :type valid_round_trips: str
        """
        self._valid_round_trips = valid_round_trips

    @property
    def endorsement_valid_period(self):
        r"""Gets the endorsement_valid_period of this ExitEntryPermitEndorsementInfo.

        签注有效期。 

        :return: The endorsement_valid_period of this ExitEntryPermitEndorsementInfo.
        :rtype: str
        """
        return self._endorsement_valid_period

    @endorsement_valid_period.setter
    def endorsement_valid_period(self, endorsement_valid_period):
        r"""Sets the endorsement_valid_period of this ExitEntryPermitEndorsementInfo.

        签注有效期。 

        :param endorsement_valid_period: The endorsement_valid_period of this ExitEntryPermitEndorsementInfo.
        :type endorsement_valid_period: str
        """
        self._endorsement_valid_period = endorsement_valid_period

    @property
    def remark(self):
        r"""Gets the remark of this ExitEntryPermitEndorsementInfo.

        签注备注。 

        :return: The remark of this ExitEntryPermitEndorsementInfo.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this ExitEntryPermitEndorsementInfo.

        签注备注。 

        :param remark: The remark of this ExitEntryPermitEndorsementInfo.
        :type remark: str
        """
        self._remark = remark

    @property
    def issue_info(self):
        r"""Gets the issue_info of this ExitEntryPermitEndorsementInfo.

        签注签发信息。 

        :return: The issue_info of this ExitEntryPermitEndorsementInfo.
        :rtype: str
        """
        return self._issue_info

    @issue_info.setter
    def issue_info(self, issue_info):
        r"""Sets the issue_info of this ExitEntryPermitEndorsementInfo.

        签注签发信息。 

        :param issue_info: The issue_info of this ExitEntryPermitEndorsementInfo.
        :type issue_info: str
        """
        self._issue_info = issue_info

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
        if not isinstance(other, ExitEntryPermitEndorsementInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
