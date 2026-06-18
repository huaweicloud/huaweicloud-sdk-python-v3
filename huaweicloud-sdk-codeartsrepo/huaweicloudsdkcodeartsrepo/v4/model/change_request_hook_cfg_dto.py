# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeRequestHookCfgDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_cfgs': 'list[WebHookEventCfgDto]',
        'project_cfgs': 'list[WebHookBranchCfgDto]',
        'branch_cfgs': 'list[WebHookBranchCfgDto]'
    }

    attribute_map = {
        'event_cfgs': 'event_cfgs',
        'project_cfgs': 'project_cfgs',
        'branch_cfgs': 'branch_cfgs'
    }

    def __init__(self, event_cfgs=None, project_cfgs=None, branch_cfgs=None):
        r"""ChangeRequestHookCfgDto

        The model defined in huaweicloud sdk

        :param event_cfgs: **参数解释：** 预留字段，事件触发设置，可为空。
        :type event_cfgs: list[:class:`huaweicloudsdkcodeartsrepo.v4.WebHookEventCfgDto`]
        :param project_cfgs: **参数解释：** 预留字段，仓库分支规则设置，可为空。
        :type project_cfgs: list[:class:`huaweicloudsdkcodeartsrepo.v4.WebHookBranchCfgDto`]
        :param branch_cfgs: 
        :type branch_cfgs: list[:class:`huaweicloudsdkcodeartsrepo.v4.WebHookBranchCfgDto`]
        """
        
        

        self._event_cfgs = None
        self._project_cfgs = None
        self._branch_cfgs = None
        self.discriminator = None

        if event_cfgs is not None:
            self.event_cfgs = event_cfgs
        if project_cfgs is not None:
            self.project_cfgs = project_cfgs
        if branch_cfgs is not None:
            self.branch_cfgs = branch_cfgs

    @property
    def event_cfgs(self):
        r"""Gets the event_cfgs of this ChangeRequestHookCfgDto.

        **参数解释：** 预留字段，事件触发设置，可为空。

        :return: The event_cfgs of this ChangeRequestHookCfgDto.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.WebHookEventCfgDto`]
        """
        return self._event_cfgs

    @event_cfgs.setter
    def event_cfgs(self, event_cfgs):
        r"""Sets the event_cfgs of this ChangeRequestHookCfgDto.

        **参数解释：** 预留字段，事件触发设置，可为空。

        :param event_cfgs: The event_cfgs of this ChangeRequestHookCfgDto.
        :type event_cfgs: list[:class:`huaweicloudsdkcodeartsrepo.v4.WebHookEventCfgDto`]
        """
        self._event_cfgs = event_cfgs

    @property
    def project_cfgs(self):
        r"""Gets the project_cfgs of this ChangeRequestHookCfgDto.

        **参数解释：** 预留字段，仓库分支规则设置，可为空。

        :return: The project_cfgs of this ChangeRequestHookCfgDto.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.WebHookBranchCfgDto`]
        """
        return self._project_cfgs

    @project_cfgs.setter
    def project_cfgs(self, project_cfgs):
        r"""Sets the project_cfgs of this ChangeRequestHookCfgDto.

        **参数解释：** 预留字段，仓库分支规则设置，可为空。

        :param project_cfgs: The project_cfgs of this ChangeRequestHookCfgDto.
        :type project_cfgs: list[:class:`huaweicloudsdkcodeartsrepo.v4.WebHookBranchCfgDto`]
        """
        self._project_cfgs = project_cfgs

    @property
    def branch_cfgs(self):
        r"""Gets the branch_cfgs of this ChangeRequestHookCfgDto.

        :return: The branch_cfgs of this ChangeRequestHookCfgDto.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.WebHookBranchCfgDto`]
        """
        return self._branch_cfgs

    @branch_cfgs.setter
    def branch_cfgs(self, branch_cfgs):
        r"""Sets the branch_cfgs of this ChangeRequestHookCfgDto.

        :param branch_cfgs: The branch_cfgs of this ChangeRequestHookCfgDto.
        :type branch_cfgs: list[:class:`huaweicloudsdkcodeartsrepo.v4.WebHookBranchCfgDto`]
        """
        self._branch_cfgs = branch_cfgs

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
        if not isinstance(other, ChangeRequestHookCfgDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
