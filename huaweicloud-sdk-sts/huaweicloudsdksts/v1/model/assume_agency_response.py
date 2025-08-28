# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssumeAgencyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_identity': 'str',
        'assumed_agency': 'AssumedAgencyDto',
        'credentials': 'CredentialsDto'
    }

    attribute_map = {
        'source_identity': 'source_identity',
        'assumed_agency': 'assumed_agency',
        'credentials': 'credentials'
    }

    def __init__(self, source_identity=None, assumed_agency=None, credentials=None):
        r"""AssumeAgencyResponse

        The model defined in huaweicloud sdk

        :param source_identity: 调用链里最初调用者所声明的身份。
        :type source_identity: str
        :param assumed_agency: 
        :type assumed_agency: :class:`huaweicloudsdksts.v1.AssumedAgencyDto`
        :param credentials: 
        :type credentials: :class:`huaweicloudsdksts.v1.CredentialsDto`
        """
        
        super(AssumeAgencyResponse, self).__init__()

        self._source_identity = None
        self._assumed_agency = None
        self._credentials = None
        self.discriminator = None

        if source_identity is not None:
            self.source_identity = source_identity
        if assumed_agency is not None:
            self.assumed_agency = assumed_agency
        if credentials is not None:
            self.credentials = credentials

    @property
    def source_identity(self):
        r"""Gets the source_identity of this AssumeAgencyResponse.

        调用链里最初调用者所声明的身份。

        :return: The source_identity of this AssumeAgencyResponse.
        :rtype: str
        """
        return self._source_identity

    @source_identity.setter
    def source_identity(self, source_identity):
        r"""Sets the source_identity of this AssumeAgencyResponse.

        调用链里最初调用者所声明的身份。

        :param source_identity: The source_identity of this AssumeAgencyResponse.
        :type source_identity: str
        """
        self._source_identity = source_identity

    @property
    def assumed_agency(self):
        r"""Gets the assumed_agency of this AssumeAgencyResponse.

        :return: The assumed_agency of this AssumeAgencyResponse.
        :rtype: :class:`huaweicloudsdksts.v1.AssumedAgencyDto`
        """
        return self._assumed_agency

    @assumed_agency.setter
    def assumed_agency(self, assumed_agency):
        r"""Sets the assumed_agency of this AssumeAgencyResponse.

        :param assumed_agency: The assumed_agency of this AssumeAgencyResponse.
        :type assumed_agency: :class:`huaweicloudsdksts.v1.AssumedAgencyDto`
        """
        self._assumed_agency = assumed_agency

    @property
    def credentials(self):
        r"""Gets the credentials of this AssumeAgencyResponse.

        :return: The credentials of this AssumeAgencyResponse.
        :rtype: :class:`huaweicloudsdksts.v1.CredentialsDto`
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        r"""Sets the credentials of this AssumeAgencyResponse.

        :param credentials: The credentials of this AssumeAgencyResponse.
        :type credentials: :class:`huaweicloudsdksts.v1.CredentialsDto`
        """
        self._credentials = credentials

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
        if not isinstance(other, AssumeAgencyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
