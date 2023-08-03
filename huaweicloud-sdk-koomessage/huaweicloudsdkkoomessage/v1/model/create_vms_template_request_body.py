# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVmsTemplateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'expiration_time': 'str',
        'tpl_name': 'str',
        'title': 'str',
        'reslist': 'list[ResourceInfo]',
        'remarks': 'str',
        'callbackurl': 'str'
    }

    attribute_map = {
        'expiration_time': 'expiration_time',
        'tpl_name': 'tpl_name',
        'title': 'title',
        'reslist': 'reslist',
        'remarks': 'remarks',
        'callbackurl': 'callbackurl'
    }

    def __init__(self, expiration_time=None, tpl_name=None, title=None, reslist=None, remarks=None, callbackurl=None):
        """CreateVmsTemplateRequestBody

        The model defined in huaweicloud sdk

        :param expiration_time: 智能信息基础版模板有效期。单位：天，必须取整，最长9999天。
        :type expiration_time: str
        :param tpl_name: 智能信息基础版模板名称。模板的别名，用来帮助记忆。最大不超过100个字，若使用中文需经过UTF-8编码。
        :type tpl_name: str
        :param title: 智能信息基础版模板主题，最大不超过20个字，若使用中文需经过UTF-8 编码，主题不能包含“【】”，否则审核会不通过。
        :type title: str
        :param reslist:  模板资源列表，由按顺序排列的资源组成，资源类型支持文本、图片、音频、视频。  &gt; 资源在JSON数组中的顺序将决定其在手机上的显示顺序，数组大小不能超过10。 
        :type reslist: list[:class:`huaweicloudsdkkoomessage.v1.ResourceInfo`]
        :param remarks: 智能信息基础版模板备注信息，用于填写对模板审核的期望或要求，最大不超过200个字。例如：希望这个模板绑定的通道类型是三网合一通道，默认优先绑定三网合一通道。
        :type remarks: str
        :param callbackurl: 客户系统回调URL，可用于通知对端模板审核状态信息。  &gt; 接口规格需参照定义智能信息基础版模板状态回执完成实现。 
        :type callbackurl: str
        """
        
        

        self._expiration_time = None
        self._tpl_name = None
        self._title = None
        self._reslist = None
        self._remarks = None
        self._callbackurl = None
        self.discriminator = None

        self.expiration_time = expiration_time
        self.tpl_name = tpl_name
        self.title = title
        self.reslist = reslist
        if remarks is not None:
            self.remarks = remarks
        if callbackurl is not None:
            self.callbackurl = callbackurl

    @property
    def expiration_time(self):
        """Gets the expiration_time of this CreateVmsTemplateRequestBody.

        智能信息基础版模板有效期。单位：天，必须取整，最长9999天。

        :return: The expiration_time of this CreateVmsTemplateRequestBody.
        :rtype: str
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this CreateVmsTemplateRequestBody.

        智能信息基础版模板有效期。单位：天，必须取整，最长9999天。

        :param expiration_time: The expiration_time of this CreateVmsTemplateRequestBody.
        :type expiration_time: str
        """
        self._expiration_time = expiration_time

    @property
    def tpl_name(self):
        """Gets the tpl_name of this CreateVmsTemplateRequestBody.

        智能信息基础版模板名称。模板的别名，用来帮助记忆。最大不超过100个字，若使用中文需经过UTF-8编码。

        :return: The tpl_name of this CreateVmsTemplateRequestBody.
        :rtype: str
        """
        return self._tpl_name

    @tpl_name.setter
    def tpl_name(self, tpl_name):
        """Sets the tpl_name of this CreateVmsTemplateRequestBody.

        智能信息基础版模板名称。模板的别名，用来帮助记忆。最大不超过100个字，若使用中文需经过UTF-8编码。

        :param tpl_name: The tpl_name of this CreateVmsTemplateRequestBody.
        :type tpl_name: str
        """
        self._tpl_name = tpl_name

    @property
    def title(self):
        """Gets the title of this CreateVmsTemplateRequestBody.

        智能信息基础版模板主题，最大不超过20个字，若使用中文需经过UTF-8 编码，主题不能包含“【】”，否则审核会不通过。

        :return: The title of this CreateVmsTemplateRequestBody.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreateVmsTemplateRequestBody.

        智能信息基础版模板主题，最大不超过20个字，若使用中文需经过UTF-8 编码，主题不能包含“【】”，否则审核会不通过。

        :param title: The title of this CreateVmsTemplateRequestBody.
        :type title: str
        """
        self._title = title

    @property
    def reslist(self):
        """Gets the reslist of this CreateVmsTemplateRequestBody.

         模板资源列表，由按顺序排列的资源组成，资源类型支持文本、图片、音频、视频。  > 资源在JSON数组中的顺序将决定其在手机上的显示顺序，数组大小不能超过10。 

        :return: The reslist of this CreateVmsTemplateRequestBody.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.ResourceInfo`]
        """
        return self._reslist

    @reslist.setter
    def reslist(self, reslist):
        """Sets the reslist of this CreateVmsTemplateRequestBody.

         模板资源列表，由按顺序排列的资源组成，资源类型支持文本、图片、音频、视频。  > 资源在JSON数组中的顺序将决定其在手机上的显示顺序，数组大小不能超过10。 

        :param reslist: The reslist of this CreateVmsTemplateRequestBody.
        :type reslist: list[:class:`huaweicloudsdkkoomessage.v1.ResourceInfo`]
        """
        self._reslist = reslist

    @property
    def remarks(self):
        """Gets the remarks of this CreateVmsTemplateRequestBody.

        智能信息基础版模板备注信息，用于填写对模板审核的期望或要求，最大不超过200个字。例如：希望这个模板绑定的通道类型是三网合一通道，默认优先绑定三网合一通道。

        :return: The remarks of this CreateVmsTemplateRequestBody.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this CreateVmsTemplateRequestBody.

        智能信息基础版模板备注信息，用于填写对模板审核的期望或要求，最大不超过200个字。例如：希望这个模板绑定的通道类型是三网合一通道，默认优先绑定三网合一通道。

        :param remarks: The remarks of this CreateVmsTemplateRequestBody.
        :type remarks: str
        """
        self._remarks = remarks

    @property
    def callbackurl(self):
        """Gets the callbackurl of this CreateVmsTemplateRequestBody.

        客户系统回调URL，可用于通知对端模板审核状态信息。  > 接口规格需参照定义智能信息基础版模板状态回执完成实现。 

        :return: The callbackurl of this CreateVmsTemplateRequestBody.
        :rtype: str
        """
        return self._callbackurl

    @callbackurl.setter
    def callbackurl(self, callbackurl):
        """Sets the callbackurl of this CreateVmsTemplateRequestBody.

        客户系统回调URL，可用于通知对端模板审核状态信息。  > 接口规格需参照定义智能信息基础版模板状态回执完成实现。 

        :param callbackurl: The callbackurl of this CreateVmsTemplateRequestBody.
        :type callbackurl: str
        """
        self._callbackurl = callbackurl

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
        if not isinstance(other, CreateVmsTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
