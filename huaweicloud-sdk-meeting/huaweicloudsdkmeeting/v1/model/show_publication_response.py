# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPublicationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'last_updated_by': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'publish_name': 'str',
        'publish_scope': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'publish_status': 'str',
        'program_list': 'list[ProgramResponseBase]',
        'dept_list': 'list[PublishDeptResponseDTO]',
        'device_list': 'list[PublishDeviceResponseDTO]'
    }

    attribute_map = {
        'id': 'id',
        'last_updated_by': 'lastUpdatedBy',
        'create_time': 'createTime',
        'update_time': 'updateTime',
        'publish_name': 'publishName',
        'publish_scope': 'publishScope',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'publish_status': 'publishStatus',
        'program_list': 'programList',
        'dept_list': 'deptList',
        'device_list': 'deviceList'
    }

    def __init__(self, id=None, last_updated_by=None, create_time=None, update_time=None, publish_name=None, publish_scope=None, start_time=None, end_time=None, publish_status=None, program_list=None, dept_list=None, device_list=None):
        """ShowPublicationResponse

        The model defined in huaweicloud sdk

        :param id: 发布ID。
        :type id: str
        :param last_updated_by: 更新者。
        :type last_updated_by: str
        :param create_time: 创建时间。
        :type create_time: int
        :param update_time: 更新时间。
        :type update_time: int
        :param publish_name: 发布名称。
        :type publish_name: str
        :param publish_scope: 发布范围。
        :type publish_scope: str
        :param start_time: 开始时间。
        :type start_time: int
        :param end_time: 结束时间。
        :type end_time: int
        :param publish_status: 根据当前时间确定发布状态。 - NOT_ONLINE-未上线 - PUBLISHING-发布中 - ALREADY_OFFLINE-已下线
        :type publish_status: str
        :param program_list: 发布节目ID列表。
        :type program_list: list[:class:`huaweicloudsdkmeeting.v1.ProgramResponseBase`]
        :param dept_list: 发布部门列表。
        :type dept_list: list[:class:`huaweicloudsdkmeeting.v1.PublishDeptResponseDTO`]
        :param device_list: 发布设备列表。
        :type device_list: list[:class:`huaweicloudsdkmeeting.v1.PublishDeviceResponseDTO`]
        """
        
        super(ShowPublicationResponse, self).__init__()

        self._id = None
        self._last_updated_by = None
        self._create_time = None
        self._update_time = None
        self._publish_name = None
        self._publish_scope = None
        self._start_time = None
        self._end_time = None
        self._publish_status = None
        self._program_list = None
        self._dept_list = None
        self._device_list = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if last_updated_by is not None:
            self.last_updated_by = last_updated_by
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if publish_name is not None:
            self.publish_name = publish_name
        if publish_scope is not None:
            self.publish_scope = publish_scope
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if publish_status is not None:
            self.publish_status = publish_status
        if program_list is not None:
            self.program_list = program_list
        if dept_list is not None:
            self.dept_list = dept_list
        if device_list is not None:
            self.device_list = device_list

    @property
    def id(self):
        """Gets the id of this ShowPublicationResponse.

        发布ID。

        :return: The id of this ShowPublicationResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowPublicationResponse.

        发布ID。

        :param id: The id of this ShowPublicationResponse.
        :type id: str
        """
        self._id = id

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this ShowPublicationResponse.

        更新者。

        :return: The last_updated_by of this ShowPublicationResponse.
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this ShowPublicationResponse.

        更新者。

        :param last_updated_by: The last_updated_by of this ShowPublicationResponse.
        :type last_updated_by: str
        """
        self._last_updated_by = last_updated_by

    @property
    def create_time(self):
        """Gets the create_time of this ShowPublicationResponse.

        创建时间。

        :return: The create_time of this ShowPublicationResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowPublicationResponse.

        创建时间。

        :param create_time: The create_time of this ShowPublicationResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowPublicationResponse.

        更新时间。

        :return: The update_time of this ShowPublicationResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowPublicationResponse.

        更新时间。

        :param update_time: The update_time of this ShowPublicationResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def publish_name(self):
        """Gets the publish_name of this ShowPublicationResponse.

        发布名称。

        :return: The publish_name of this ShowPublicationResponse.
        :rtype: str
        """
        return self._publish_name

    @publish_name.setter
    def publish_name(self, publish_name):
        """Sets the publish_name of this ShowPublicationResponse.

        发布名称。

        :param publish_name: The publish_name of this ShowPublicationResponse.
        :type publish_name: str
        """
        self._publish_name = publish_name

    @property
    def publish_scope(self):
        """Gets the publish_scope of this ShowPublicationResponse.

        发布范围。

        :return: The publish_scope of this ShowPublicationResponse.
        :rtype: str
        """
        return self._publish_scope

    @publish_scope.setter
    def publish_scope(self, publish_scope):
        """Sets the publish_scope of this ShowPublicationResponse.

        发布范围。

        :param publish_scope: The publish_scope of this ShowPublicationResponse.
        :type publish_scope: str
        """
        self._publish_scope = publish_scope

    @property
    def start_time(self):
        """Gets the start_time of this ShowPublicationResponse.

        开始时间。

        :return: The start_time of this ShowPublicationResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowPublicationResponse.

        开始时间。

        :param start_time: The start_time of this ShowPublicationResponse.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowPublicationResponse.

        结束时间。

        :return: The end_time of this ShowPublicationResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowPublicationResponse.

        结束时间。

        :param end_time: The end_time of this ShowPublicationResponse.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def publish_status(self):
        """Gets the publish_status of this ShowPublicationResponse.

        根据当前时间确定发布状态。 - NOT_ONLINE-未上线 - PUBLISHING-发布中 - ALREADY_OFFLINE-已下线

        :return: The publish_status of this ShowPublicationResponse.
        :rtype: str
        """
        return self._publish_status

    @publish_status.setter
    def publish_status(self, publish_status):
        """Sets the publish_status of this ShowPublicationResponse.

        根据当前时间确定发布状态。 - NOT_ONLINE-未上线 - PUBLISHING-发布中 - ALREADY_OFFLINE-已下线

        :param publish_status: The publish_status of this ShowPublicationResponse.
        :type publish_status: str
        """
        self._publish_status = publish_status

    @property
    def program_list(self):
        """Gets the program_list of this ShowPublicationResponse.

        发布节目ID列表。

        :return: The program_list of this ShowPublicationResponse.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.ProgramResponseBase`]
        """
        return self._program_list

    @program_list.setter
    def program_list(self, program_list):
        """Sets the program_list of this ShowPublicationResponse.

        发布节目ID列表。

        :param program_list: The program_list of this ShowPublicationResponse.
        :type program_list: list[:class:`huaweicloudsdkmeeting.v1.ProgramResponseBase`]
        """
        self._program_list = program_list

    @property
    def dept_list(self):
        """Gets the dept_list of this ShowPublicationResponse.

        发布部门列表。

        :return: The dept_list of this ShowPublicationResponse.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.PublishDeptResponseDTO`]
        """
        return self._dept_list

    @dept_list.setter
    def dept_list(self, dept_list):
        """Sets the dept_list of this ShowPublicationResponse.

        发布部门列表。

        :param dept_list: The dept_list of this ShowPublicationResponse.
        :type dept_list: list[:class:`huaweicloudsdkmeeting.v1.PublishDeptResponseDTO`]
        """
        self._dept_list = dept_list

    @property
    def device_list(self):
        """Gets the device_list of this ShowPublicationResponse.

        发布设备列表。

        :return: The device_list of this ShowPublicationResponse.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.PublishDeviceResponseDTO`]
        """
        return self._device_list

    @device_list.setter
    def device_list(self, device_list):
        """Sets the device_list of this ShowPublicationResponse.

        发布设备列表。

        :param device_list: The device_list of this ShowPublicationResponse.
        :type device_list: list[:class:`huaweicloudsdkmeeting.v1.PublishDeviceResponseDTO`]
        """
        self._device_list = device_list

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
        if not isinstance(other, ShowPublicationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
