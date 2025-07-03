# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPrecheckResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result_code': 'int',
        'status': 'str',
        'updated_at': 'str',
        'display': 'bool',
        'instance_status_check_list': 'list[str]',
        'db_upgrade_precheck': 'DBUpgradePrecheck',
        'download_link': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'result_code': 'result_code',
        'status': 'status',
        'updated_at': 'updated_at',
        'display': 'display',
        'instance_status_check_list': 'instance_status_check_list',
        'db_upgrade_precheck': 'db_upgrade_precheck',
        'download_link': 'download_link',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, result_code=None, status=None, updated_at=None, display=None, instance_status_check_list=None, db_upgrade_precheck=None, download_link=None, x_request_id=None):
        r"""ShowPrecheckResultResponse

        The model defined in huaweicloud sdk

        :param result_code: 检查是否通过，0代表通过，1代表未通过
        :type result_code: int
        :param status: 检查状态
        :type status: str
        :param updated_at: 检查结果更新时间
        :type updated_at: str
        :param display: 是否展示数据库检查结果
        :type display: bool
        :param instance_status_check_list: 实例关联关系检查失败项
        :type instance_status_check_list: list[str]
        :param db_upgrade_precheck: 
        :type db_upgrade_precheck: :class:`huaweicloudsdkrds.v3.DBUpgradePrecheck`
        :param download_link: 检查结果下载链接
        :type download_link: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowPrecheckResultResponse, self).__init__()

        self._result_code = None
        self._status = None
        self._updated_at = None
        self._display = None
        self._instance_status_check_list = None
        self._db_upgrade_precheck = None
        self._download_link = None
        self._x_request_id = None
        self.discriminator = None

        if result_code is not None:
            self.result_code = result_code
        if status is not None:
            self.status = status
        if updated_at is not None:
            self.updated_at = updated_at
        if display is not None:
            self.display = display
        if instance_status_check_list is not None:
            self.instance_status_check_list = instance_status_check_list
        if db_upgrade_precheck is not None:
            self.db_upgrade_precheck = db_upgrade_precheck
        if download_link is not None:
            self.download_link = download_link
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def result_code(self):
        r"""Gets the result_code of this ShowPrecheckResultResponse.

        检查是否通过，0代表通过，1代表未通过

        :return: The result_code of this ShowPrecheckResultResponse.
        :rtype: int
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        r"""Sets the result_code of this ShowPrecheckResultResponse.

        检查是否通过，0代表通过，1代表未通过

        :param result_code: The result_code of this ShowPrecheckResultResponse.
        :type result_code: int
        """
        self._result_code = result_code

    @property
    def status(self):
        r"""Gets the status of this ShowPrecheckResultResponse.

        检查状态

        :return: The status of this ShowPrecheckResultResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowPrecheckResultResponse.

        检查状态

        :param status: The status of this ShowPrecheckResultResponse.
        :type status: str
        """
        self._status = status

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowPrecheckResultResponse.

        检查结果更新时间

        :return: The updated_at of this ShowPrecheckResultResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowPrecheckResultResponse.

        检查结果更新时间

        :param updated_at: The updated_at of this ShowPrecheckResultResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def display(self):
        r"""Gets the display of this ShowPrecheckResultResponse.

        是否展示数据库检查结果

        :return: The display of this ShowPrecheckResultResponse.
        :rtype: bool
        """
        return self._display

    @display.setter
    def display(self, display):
        r"""Sets the display of this ShowPrecheckResultResponse.

        是否展示数据库检查结果

        :param display: The display of this ShowPrecheckResultResponse.
        :type display: bool
        """
        self._display = display

    @property
    def instance_status_check_list(self):
        r"""Gets the instance_status_check_list of this ShowPrecheckResultResponse.

        实例关联关系检查失败项

        :return: The instance_status_check_list of this ShowPrecheckResultResponse.
        :rtype: list[str]
        """
        return self._instance_status_check_list

    @instance_status_check_list.setter
    def instance_status_check_list(self, instance_status_check_list):
        r"""Sets the instance_status_check_list of this ShowPrecheckResultResponse.

        实例关联关系检查失败项

        :param instance_status_check_list: The instance_status_check_list of this ShowPrecheckResultResponse.
        :type instance_status_check_list: list[str]
        """
        self._instance_status_check_list = instance_status_check_list

    @property
    def db_upgrade_precheck(self):
        r"""Gets the db_upgrade_precheck of this ShowPrecheckResultResponse.

        :return: The db_upgrade_precheck of this ShowPrecheckResultResponse.
        :rtype: :class:`huaweicloudsdkrds.v3.DBUpgradePrecheck`
        """
        return self._db_upgrade_precheck

    @db_upgrade_precheck.setter
    def db_upgrade_precheck(self, db_upgrade_precheck):
        r"""Sets the db_upgrade_precheck of this ShowPrecheckResultResponse.

        :param db_upgrade_precheck: The db_upgrade_precheck of this ShowPrecheckResultResponse.
        :type db_upgrade_precheck: :class:`huaweicloudsdkrds.v3.DBUpgradePrecheck`
        """
        self._db_upgrade_precheck = db_upgrade_precheck

    @property
    def download_link(self):
        r"""Gets the download_link of this ShowPrecheckResultResponse.

        检查结果下载链接

        :return: The download_link of this ShowPrecheckResultResponse.
        :rtype: str
        """
        return self._download_link

    @download_link.setter
    def download_link(self, download_link):
        r"""Sets the download_link of this ShowPrecheckResultResponse.

        检查结果下载链接

        :param download_link: The download_link of this ShowPrecheckResultResponse.
        :type download_link: str
        """
        self._download_link = download_link

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowPrecheckResultResponse.

        :return: The x_request_id of this ShowPrecheckResultResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowPrecheckResultResponse.

        :param x_request_id: The x_request_id of this ShowPrecheckResultResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowPrecheckResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
