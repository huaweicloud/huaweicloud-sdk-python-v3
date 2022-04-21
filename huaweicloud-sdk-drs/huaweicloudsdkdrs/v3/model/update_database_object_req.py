# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDatabaseObjectReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'selected': 'bool',
        'sync_database': 'bool',
        'job': 'list[DatabaseInfo]'
    }

    attribute_map = {
        'job_id': 'job_id',
        'selected': 'selected',
        'sync_database': 'sync_database',
        'job': 'job'
    }

    def __init__(self, job_id=None, selected=None, sync_database=None, job=None):
        """UpdateDatabaseObjectReq

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param selected: 是否进行对象选择，是：自定义迁移对象，否：全部迁移，不填默认为否。
        :type selected: bool
        :param sync_database: 是否库级同步
        :type sync_database: bool
        :param job: 数据对象选择信息，selected为true时必填。
        :type job: list[:class:`huaweicloudsdkdrs.v3.DatabaseInfo`]
        """
        
        

        self._job_id = None
        self._selected = None
        self._sync_database = None
        self._job = None
        self.discriminator = None

        self.job_id = job_id
        if selected is not None:
            self.selected = selected
        if sync_database is not None:
            self.sync_database = sync_database
        if job is not None:
            self.job = job

    @property
    def job_id(self):
        """Gets the job_id of this UpdateDatabaseObjectReq.

        任务ID

        :return: The job_id of this UpdateDatabaseObjectReq.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this UpdateDatabaseObjectReq.

        任务ID

        :param job_id: The job_id of this UpdateDatabaseObjectReq.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def selected(self):
        """Gets the selected of this UpdateDatabaseObjectReq.

        是否进行对象选择，是：自定义迁移对象，否：全部迁移，不填默认为否。

        :return: The selected of this UpdateDatabaseObjectReq.
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this UpdateDatabaseObjectReq.

        是否进行对象选择，是：自定义迁移对象，否：全部迁移，不填默认为否。

        :param selected: The selected of this UpdateDatabaseObjectReq.
        :type selected: bool
        """
        self._selected = selected

    @property
    def sync_database(self):
        """Gets the sync_database of this UpdateDatabaseObjectReq.

        是否库级同步

        :return: The sync_database of this UpdateDatabaseObjectReq.
        :rtype: bool
        """
        return self._sync_database

    @sync_database.setter
    def sync_database(self, sync_database):
        """Sets the sync_database of this UpdateDatabaseObjectReq.

        是否库级同步

        :param sync_database: The sync_database of this UpdateDatabaseObjectReq.
        :type sync_database: bool
        """
        self._sync_database = sync_database

    @property
    def job(self):
        """Gets the job of this UpdateDatabaseObjectReq.

        数据对象选择信息，selected为true时必填。

        :return: The job of this UpdateDatabaseObjectReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.DatabaseInfo`]
        """
        return self._job

    @job.setter
    def job(self, job):
        """Sets the job of this UpdateDatabaseObjectReq.

        数据对象选择信息，selected为true时必填。

        :param job: The job of this UpdateDatabaseObjectReq.
        :type job: list[:class:`huaweicloudsdkdrs.v3.DatabaseInfo`]
        """
        self._job = job

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
        if not isinstance(other, UpdateDatabaseObjectReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
