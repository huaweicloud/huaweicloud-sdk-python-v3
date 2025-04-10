# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoints': 'list[JobEndpointInfo]',
        'precheck_mode': 'str',
        'skip_precheck_info': 'SkipPreCheckInfo',
        'pause_mode': 'str',
        'start_time': 'str',
        'compare_task_param': 'CompareTaskParams',
        'is_sync_re_edit': 'bool',
        'is_only_init_task': 'bool',
        'force_delete': 'bool',
        'public_ip_config': 'PublicIpConfig',
        'replay_config': 'ReplayConfigInfo',
        'repair_info': 'ActionParamsRepairInfo'
    }

    attribute_map = {
        'endpoints': 'endpoints',
        'precheck_mode': 'precheck_mode',
        'skip_precheck_info': 'skip_precheck_info',
        'pause_mode': 'pause_mode',
        'start_time': 'start_time',
        'compare_task_param': 'compare_task_param',
        'is_sync_re_edit': 'is_sync_re_edit',
        'is_only_init_task': 'is_only_init_task',
        'force_delete': 'force_delete',
        'public_ip_config': 'public_ip_config',
        'replay_config': 'replay_config',
        'repair_info': 'repair_info'
    }

    def __init__(self, endpoints=None, precheck_mode=None, skip_precheck_info=None, pause_mode=None, start_time=None, compare_task_param=None, is_sync_re_edit=None, is_only_init_task=None, force_delete=None, public_ip_config=None, replay_config=None, repair_info=None):
        r"""ActionParams

        The model defined in huaweicloud sdk

        :param endpoints: 测试连接数据库信息。
        :type endpoints: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        :param precheck_mode: 预检查模式。
        :type precheck_mode: str
        :param skip_precheck_info: 
        :type skip_precheck_info: :class:`huaweicloudsdkdrs.v5.SkipPreCheckInfo`
        :param pause_mode: 任务暂停模式。
        :type pause_mode: str
        :param start_time: 任务定时启动时间。
        :type start_time: str
        :param compare_task_param: 
        :type compare_task_param: :class:`huaweicloudsdkdrs.v5.CompareTaskParams`
        :param is_sync_re_edit: 再编辑任务启动时取值true。
        :type is_sync_re_edit: bool
        :param is_only_init_task: 是否支持只初始化任务。仅支持白名单用户使用，需要提交工单申请才能使用。
        :type is_only_init_task: bool
        :param force_delete: 强制结束时取值为true。
        :type force_delete: bool
        :param public_ip_config: 
        :type public_ip_config: :class:`huaweicloudsdkdrs.v5.PublicIpConfig`
        :param replay_config: 
        :type replay_config: :class:`huaweicloudsdkdrs.v5.ReplayConfigInfo`
        :param repair_info: 
        :type repair_info: :class:`huaweicloudsdkdrs.v5.ActionParamsRepairInfo`
        """
        
        

        self._endpoints = None
        self._precheck_mode = None
        self._skip_precheck_info = None
        self._pause_mode = None
        self._start_time = None
        self._compare_task_param = None
        self._is_sync_re_edit = None
        self._is_only_init_task = None
        self._force_delete = None
        self._public_ip_config = None
        self._replay_config = None
        self._repair_info = None
        self.discriminator = None

        if endpoints is not None:
            self.endpoints = endpoints
        if precheck_mode is not None:
            self.precheck_mode = precheck_mode
        if skip_precheck_info is not None:
            self.skip_precheck_info = skip_precheck_info
        if pause_mode is not None:
            self.pause_mode = pause_mode
        if start_time is not None:
            self.start_time = start_time
        if compare_task_param is not None:
            self.compare_task_param = compare_task_param
        if is_sync_re_edit is not None:
            self.is_sync_re_edit = is_sync_re_edit
        if is_only_init_task is not None:
            self.is_only_init_task = is_only_init_task
        if force_delete is not None:
            self.force_delete = force_delete
        if public_ip_config is not None:
            self.public_ip_config = public_ip_config
        if replay_config is not None:
            self.replay_config = replay_config
        if repair_info is not None:
            self.repair_info = repair_info

    @property
    def endpoints(self):
        r"""Gets the endpoints of this ActionParams.

        测试连接数据库信息。

        :return: The endpoints of this ActionParams.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        r"""Sets the endpoints of this ActionParams.

        测试连接数据库信息。

        :param endpoints: The endpoints of this ActionParams.
        :type endpoints: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        """
        self._endpoints = endpoints

    @property
    def precheck_mode(self):
        r"""Gets the precheck_mode of this ActionParams.

        预检查模式。

        :return: The precheck_mode of this ActionParams.
        :rtype: str
        """
        return self._precheck_mode

    @precheck_mode.setter
    def precheck_mode(self, precheck_mode):
        r"""Sets the precheck_mode of this ActionParams.

        预检查模式。

        :param precheck_mode: The precheck_mode of this ActionParams.
        :type precheck_mode: str
        """
        self._precheck_mode = precheck_mode

    @property
    def skip_precheck_info(self):
        r"""Gets the skip_precheck_info of this ActionParams.

        :return: The skip_precheck_info of this ActionParams.
        :rtype: :class:`huaweicloudsdkdrs.v5.SkipPreCheckInfo`
        """
        return self._skip_precheck_info

    @skip_precheck_info.setter
    def skip_precheck_info(self, skip_precheck_info):
        r"""Sets the skip_precheck_info of this ActionParams.

        :param skip_precheck_info: The skip_precheck_info of this ActionParams.
        :type skip_precheck_info: :class:`huaweicloudsdkdrs.v5.SkipPreCheckInfo`
        """
        self._skip_precheck_info = skip_precheck_info

    @property
    def pause_mode(self):
        r"""Gets the pause_mode of this ActionParams.

        任务暂停模式。

        :return: The pause_mode of this ActionParams.
        :rtype: str
        """
        return self._pause_mode

    @pause_mode.setter
    def pause_mode(self, pause_mode):
        r"""Sets the pause_mode of this ActionParams.

        任务暂停模式。

        :param pause_mode: The pause_mode of this ActionParams.
        :type pause_mode: str
        """
        self._pause_mode = pause_mode

    @property
    def start_time(self):
        r"""Gets the start_time of this ActionParams.

        任务定时启动时间。

        :return: The start_time of this ActionParams.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ActionParams.

        任务定时启动时间。

        :param start_time: The start_time of this ActionParams.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def compare_task_param(self):
        r"""Gets the compare_task_param of this ActionParams.

        :return: The compare_task_param of this ActionParams.
        :rtype: :class:`huaweicloudsdkdrs.v5.CompareTaskParams`
        """
        return self._compare_task_param

    @compare_task_param.setter
    def compare_task_param(self, compare_task_param):
        r"""Sets the compare_task_param of this ActionParams.

        :param compare_task_param: The compare_task_param of this ActionParams.
        :type compare_task_param: :class:`huaweicloudsdkdrs.v5.CompareTaskParams`
        """
        self._compare_task_param = compare_task_param

    @property
    def is_sync_re_edit(self):
        r"""Gets the is_sync_re_edit of this ActionParams.

        再编辑任务启动时取值true。

        :return: The is_sync_re_edit of this ActionParams.
        :rtype: bool
        """
        return self._is_sync_re_edit

    @is_sync_re_edit.setter
    def is_sync_re_edit(self, is_sync_re_edit):
        r"""Sets the is_sync_re_edit of this ActionParams.

        再编辑任务启动时取值true。

        :param is_sync_re_edit: The is_sync_re_edit of this ActionParams.
        :type is_sync_re_edit: bool
        """
        self._is_sync_re_edit = is_sync_re_edit

    @property
    def is_only_init_task(self):
        r"""Gets the is_only_init_task of this ActionParams.

        是否支持只初始化任务。仅支持白名单用户使用，需要提交工单申请才能使用。

        :return: The is_only_init_task of this ActionParams.
        :rtype: bool
        """
        return self._is_only_init_task

    @is_only_init_task.setter
    def is_only_init_task(self, is_only_init_task):
        r"""Sets the is_only_init_task of this ActionParams.

        是否支持只初始化任务。仅支持白名单用户使用，需要提交工单申请才能使用。

        :param is_only_init_task: The is_only_init_task of this ActionParams.
        :type is_only_init_task: bool
        """
        self._is_only_init_task = is_only_init_task

    @property
    def force_delete(self):
        r"""Gets the force_delete of this ActionParams.

        强制结束时取值为true。

        :return: The force_delete of this ActionParams.
        :rtype: bool
        """
        return self._force_delete

    @force_delete.setter
    def force_delete(self, force_delete):
        r"""Sets the force_delete of this ActionParams.

        强制结束时取值为true。

        :param force_delete: The force_delete of this ActionParams.
        :type force_delete: bool
        """
        self._force_delete = force_delete

    @property
    def public_ip_config(self):
        r"""Gets the public_ip_config of this ActionParams.

        :return: The public_ip_config of this ActionParams.
        :rtype: :class:`huaweicloudsdkdrs.v5.PublicIpConfig`
        """
        return self._public_ip_config

    @public_ip_config.setter
    def public_ip_config(self, public_ip_config):
        r"""Sets the public_ip_config of this ActionParams.

        :param public_ip_config: The public_ip_config of this ActionParams.
        :type public_ip_config: :class:`huaweicloudsdkdrs.v5.PublicIpConfig`
        """
        self._public_ip_config = public_ip_config

    @property
    def replay_config(self):
        r"""Gets the replay_config of this ActionParams.

        :return: The replay_config of this ActionParams.
        :rtype: :class:`huaweicloudsdkdrs.v5.ReplayConfigInfo`
        """
        return self._replay_config

    @replay_config.setter
    def replay_config(self, replay_config):
        r"""Sets the replay_config of this ActionParams.

        :param replay_config: The replay_config of this ActionParams.
        :type replay_config: :class:`huaweicloudsdkdrs.v5.ReplayConfigInfo`
        """
        self._replay_config = replay_config

    @property
    def repair_info(self):
        r"""Gets the repair_info of this ActionParams.

        :return: The repair_info of this ActionParams.
        :rtype: :class:`huaweicloudsdkdrs.v5.ActionParamsRepairInfo`
        """
        return self._repair_info

    @repair_info.setter
    def repair_info(self, repair_info):
        r"""Sets the repair_info of this ActionParams.

        :param repair_info: The repair_info of this ActionParams.
        :type repair_info: :class:`huaweicloudsdkdrs.v5.ActionParamsRepairInfo`
        """
        self._repair_info = repair_info

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
        if not isinstance(other, ActionParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
