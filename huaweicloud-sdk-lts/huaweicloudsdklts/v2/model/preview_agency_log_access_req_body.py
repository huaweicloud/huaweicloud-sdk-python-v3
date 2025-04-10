# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreviewAgencyLogAccessReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency_access_type': 'str',
        'agency_log_access': 'str',
        'log_agency_stream_name': 'str',
        'log_agency_stream_id': 'str',
        'log_agency_group_name': 'str',
        'log_agency_group_id': 'str',
        'log_be_agencystream_name': 'str',
        'log_be_agencystream_id': 'str',
        'log_be_agencygroup_name': 'str',
        'log_be_agencygroup_id': 'str',
        'be_agency_project_id': 'str',
        'agency_project_id': 'str',
        'agency_domain_name': 'str',
        'agency_name': 'str'
    }

    attribute_map = {
        'agency_access_type': 'agency_access_type',
        'agency_log_access': 'agency_log_access',
        'log_agency_stream_name': 'log_agencyStream_name',
        'log_agency_stream_id': 'log_agencyStream_id',
        'log_agency_group_name': 'log_agencyGroup_name',
        'log_agency_group_id': 'log_agencyGroup_id',
        'log_be_agencystream_name': 'log_beAgencystream_name',
        'log_be_agencystream_id': 'log_beAgencystream_id',
        'log_be_agencygroup_name': 'log_beAgencygroup_name',
        'log_be_agencygroup_id': 'log_beAgencygroup_id',
        'be_agency_project_id': 'be_agency_project_id',
        'agency_project_id': 'agency_project_id',
        'agency_domain_name': 'agency_domain_name',
        'agency_name': 'agency_name'
    }

    def __init__(self, agency_access_type=None, agency_log_access=None, log_agency_stream_name=None, log_agency_stream_id=None, log_agency_group_name=None, log_agency_group_id=None, log_be_agencystream_name=None, log_be_agencystream_id=None, log_be_agencygroup_name=None, log_be_agencygroup_id=None, be_agency_project_id=None, agency_project_id=None, agency_domain_name=None, agency_name=None):
        r"""PreviewAgencyLogAccessReqBody

        The model defined in huaweicloud sdk

        :param agency_access_type: 日志访问类型
        :type agency_access_type: str
        :param agency_log_access: 跨账号日志接入配置名称
        :type agency_log_access: str
        :param log_agency_stream_name: 委托日志流名称
        :type log_agency_stream_name: str
        :param log_agency_stream_id: 委托日志流id
        :type log_agency_stream_id: str
        :param log_agency_group_name: 委托日志组名称
        :type log_agency_group_name: str
        :param log_agency_group_id: 委托日志组id
        :type log_agency_group_id: str
        :param log_be_agencystream_name: 被委托日志流名称
        :type log_be_agencystream_name: str
        :param log_be_agencystream_id: 被委托日志流id
        :type log_be_agencystream_id: str
        :param log_be_agencygroup_name: 被委托日志组名称
        :type log_be_agencygroup_name: str
        :param log_be_agencygroup_id: 被委托日志组id
        :type log_be_agencygroup_id: str
        :param be_agency_project_id: 被委托项目id
        :type be_agency_project_id: str
        :param agency_project_id: 委托项目id
        :type agency_project_id: str
        :param agency_domain_name: 委托账号名称
        :type agency_domain_name: str
        :param agency_name: 委托名称
        :type agency_name: str
        """
        
        

        self._agency_access_type = None
        self._agency_log_access = None
        self._log_agency_stream_name = None
        self._log_agency_stream_id = None
        self._log_agency_group_name = None
        self._log_agency_group_id = None
        self._log_be_agencystream_name = None
        self._log_be_agencystream_id = None
        self._log_be_agencygroup_name = None
        self._log_be_agencygroup_id = None
        self._be_agency_project_id = None
        self._agency_project_id = None
        self._agency_domain_name = None
        self._agency_name = None
        self.discriminator = None

        self.agency_access_type = agency_access_type
        self.agency_log_access = agency_log_access
        self.log_agency_stream_name = log_agency_stream_name
        self.log_agency_stream_id = log_agency_stream_id
        self.log_agency_group_name = log_agency_group_name
        self.log_agency_group_id = log_agency_group_id
        self.log_be_agencystream_name = log_be_agencystream_name
        self.log_be_agencystream_id = log_be_agencystream_id
        self.log_be_agencygroup_name = log_be_agencygroup_name
        self.log_be_agencygroup_id = log_be_agencygroup_id
        self.be_agency_project_id = be_agency_project_id
        self.agency_project_id = agency_project_id
        self.agency_domain_name = agency_domain_name
        self.agency_name = agency_name

    @property
    def agency_access_type(self):
        r"""Gets the agency_access_type of this PreviewAgencyLogAccessReqBody.

        日志访问类型

        :return: The agency_access_type of this PreviewAgencyLogAccessReqBody.
        :rtype: str
        """
        return self._agency_access_type

    @agency_access_type.setter
    def agency_access_type(self, agency_access_type):
        r"""Sets the agency_access_type of this PreviewAgencyLogAccessReqBody.

        日志访问类型

        :param agency_access_type: The agency_access_type of this PreviewAgencyLogAccessReqBody.
        :type agency_access_type: str
        """
        self._agency_access_type = agency_access_type

    @property
    def agency_log_access(self):
        r"""Gets the agency_log_access of this PreviewAgencyLogAccessReqBody.

        跨账号日志接入配置名称

        :return: The agency_log_access of this PreviewAgencyLogAccessReqBody.
        :rtype: str
        """
        return self._agency_log_access

    @agency_log_access.setter
    def agency_log_access(self, agency_log_access):
        r"""Sets the agency_log_access of this PreviewAgencyLogAccessReqBody.

        跨账号日志接入配置名称

        :param agency_log_access: The agency_log_access of this PreviewAgencyLogAccessReqBody.
        :type agency_log_access: str
        """
        self._agency_log_access = agency_log_access

    @property
    def log_agency_stream_name(self):
        r"""Gets the log_agency_stream_name of this PreviewAgencyLogAccessReqBody.

        委托日志流名称

        :return: The log_agency_stream_name of this PreviewAgencyLogAccessReqBody.
        :rtype: str
        """
        return self._log_agency_stream_name

    @log_agency_stream_name.setter
    def log_agency_stream_name(self, log_agency_stream_name):
        r"""Sets the log_agency_stream_name of this PreviewAgencyLogAccessReqBody.

        委托日志流名称

        :param log_agency_stream_name: The log_agency_stream_name of this PreviewAgencyLogAccessReqBody.
        :type log_agency_stream_name: str
        """
        self._log_agency_stream_name = log_agency_stream_name

    @property
    def log_agency_stream_id(self):
        r"""Gets the log_agency_stream_id of this PreviewAgencyLogAccessReqBody.

        委托日志流id

        :return: The log_agency_stream_id of this PreviewAgencyLogAccessReqBody.
        :rtype: str
        """
        return self._log_agency_stream_id

    @log_agency_stream_id.setter
    def log_agency_stream_id(self, log_agency_stream_id):
        r"""Sets the log_agency_stream_id of this PreviewAgencyLogAccessReqBody.

        委托日志流id

        :param log_agency_stream_id: The log_agency_stream_id of this PreviewAgencyLogAccessReqBody.
        :type log_agency_stream_id: str
        """
        self._log_agency_stream_id = log_agency_stream_id

    @property
    def log_agency_group_name(self):
        r"""Gets the log_agency_group_name of this PreviewAgencyLogAccessReqBody.

        委托日志组名称

        :return: The log_agency_group_name of this PreviewAgencyLogAccessReqBody.
        :rtype: str
        """
        return self._log_agency_group_name

    @log_agency_group_name.setter
    def log_agency_group_name(self, log_agency_group_name):
        r"""Sets the log_agency_group_name of this PreviewAgencyLogAccessReqBody.

        委托日志组名称

        :param log_agency_group_name: The log_agency_group_name of this PreviewAgencyLogAccessReqBody.
        :type log_agency_group_name: str
        """
        self._log_agency_group_name = log_agency_group_name

    @property
    def log_agency_group_id(self):
        r"""Gets the log_agency_group_id of this PreviewAgencyLogAccessReqBody.

        委托日志组id

        :return: The log_agency_group_id of this PreviewAgencyLogAccessReqBody.
        :rtype: str
        """
        return self._log_agency_group_id

    @log_agency_group_id.setter
    def log_agency_group_id(self, log_agency_group_id):
        r"""Sets the log_agency_group_id of this PreviewAgencyLogAccessReqBody.

        委托日志组id

        :param log_agency_group_id: The log_agency_group_id of this PreviewAgencyLogAccessReqBody.
        :type log_agency_group_id: str
        """
        self._log_agency_group_id = log_agency_group_id

    @property
    def log_be_agencystream_name(self):
        r"""Gets the log_be_agencystream_name of this PreviewAgencyLogAccessReqBody.

        被委托日志流名称

        :return: The log_be_agencystream_name of this PreviewAgencyLogAccessReqBody.
        :rtype: str
        """
        return self._log_be_agencystream_name

    @log_be_agencystream_name.setter
    def log_be_agencystream_name(self, log_be_agencystream_name):
        r"""Sets the log_be_agencystream_name of this PreviewAgencyLogAccessReqBody.

        被委托日志流名称

        :param log_be_agencystream_name: The log_be_agencystream_name of this PreviewAgencyLogAccessReqBody.
        :type log_be_agencystream_name: str
        """
        self._log_be_agencystream_name = log_be_agencystream_name

    @property
    def log_be_agencystream_id(self):
        r"""Gets the log_be_agencystream_id of this PreviewAgencyLogAccessReqBody.

        被委托日志流id

        :return: The log_be_agencystream_id of this PreviewAgencyLogAccessReqBody.
        :rtype: str
        """
        return self._log_be_agencystream_id

    @log_be_agencystream_id.setter
    def log_be_agencystream_id(self, log_be_agencystream_id):
        r"""Sets the log_be_agencystream_id of this PreviewAgencyLogAccessReqBody.

        被委托日志流id

        :param log_be_agencystream_id: The log_be_agencystream_id of this PreviewAgencyLogAccessReqBody.
        :type log_be_agencystream_id: str
        """
        self._log_be_agencystream_id = log_be_agencystream_id

    @property
    def log_be_agencygroup_name(self):
        r"""Gets the log_be_agencygroup_name of this PreviewAgencyLogAccessReqBody.

        被委托日志组名称

        :return: The log_be_agencygroup_name of this PreviewAgencyLogAccessReqBody.
        :rtype: str
        """
        return self._log_be_agencygroup_name

    @log_be_agencygroup_name.setter
    def log_be_agencygroup_name(self, log_be_agencygroup_name):
        r"""Sets the log_be_agencygroup_name of this PreviewAgencyLogAccessReqBody.

        被委托日志组名称

        :param log_be_agencygroup_name: The log_be_agencygroup_name of this PreviewAgencyLogAccessReqBody.
        :type log_be_agencygroup_name: str
        """
        self._log_be_agencygroup_name = log_be_agencygroup_name

    @property
    def log_be_agencygroup_id(self):
        r"""Gets the log_be_agencygroup_id of this PreviewAgencyLogAccessReqBody.

        被委托日志组id

        :return: The log_be_agencygroup_id of this PreviewAgencyLogAccessReqBody.
        :rtype: str
        """
        return self._log_be_agencygroup_id

    @log_be_agencygroup_id.setter
    def log_be_agencygroup_id(self, log_be_agencygroup_id):
        r"""Sets the log_be_agencygroup_id of this PreviewAgencyLogAccessReqBody.

        被委托日志组id

        :param log_be_agencygroup_id: The log_be_agencygroup_id of this PreviewAgencyLogAccessReqBody.
        :type log_be_agencygroup_id: str
        """
        self._log_be_agencygroup_id = log_be_agencygroup_id

    @property
    def be_agency_project_id(self):
        r"""Gets the be_agency_project_id of this PreviewAgencyLogAccessReqBody.

        被委托项目id

        :return: The be_agency_project_id of this PreviewAgencyLogAccessReqBody.
        :rtype: str
        """
        return self._be_agency_project_id

    @be_agency_project_id.setter
    def be_agency_project_id(self, be_agency_project_id):
        r"""Sets the be_agency_project_id of this PreviewAgencyLogAccessReqBody.

        被委托项目id

        :param be_agency_project_id: The be_agency_project_id of this PreviewAgencyLogAccessReqBody.
        :type be_agency_project_id: str
        """
        self._be_agency_project_id = be_agency_project_id

    @property
    def agency_project_id(self):
        r"""Gets the agency_project_id of this PreviewAgencyLogAccessReqBody.

        委托项目id

        :return: The agency_project_id of this PreviewAgencyLogAccessReqBody.
        :rtype: str
        """
        return self._agency_project_id

    @agency_project_id.setter
    def agency_project_id(self, agency_project_id):
        r"""Sets the agency_project_id of this PreviewAgencyLogAccessReqBody.

        委托项目id

        :param agency_project_id: The agency_project_id of this PreviewAgencyLogAccessReqBody.
        :type agency_project_id: str
        """
        self._agency_project_id = agency_project_id

    @property
    def agency_domain_name(self):
        r"""Gets the agency_domain_name of this PreviewAgencyLogAccessReqBody.

        委托账号名称

        :return: The agency_domain_name of this PreviewAgencyLogAccessReqBody.
        :rtype: str
        """
        return self._agency_domain_name

    @agency_domain_name.setter
    def agency_domain_name(self, agency_domain_name):
        r"""Sets the agency_domain_name of this PreviewAgencyLogAccessReqBody.

        委托账号名称

        :param agency_domain_name: The agency_domain_name of this PreviewAgencyLogAccessReqBody.
        :type agency_domain_name: str
        """
        self._agency_domain_name = agency_domain_name

    @property
    def agency_name(self):
        r"""Gets the agency_name of this PreviewAgencyLogAccessReqBody.

        委托名称

        :return: The agency_name of this PreviewAgencyLogAccessReqBody.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this PreviewAgencyLogAccessReqBody.

        委托名称

        :param agency_name: The agency_name of this PreviewAgencyLogAccessReqBody.
        :type agency_name: str
        """
        self._agency_name = agency_name

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
        if not isinstance(other, PreviewAgencyLogAccessReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
