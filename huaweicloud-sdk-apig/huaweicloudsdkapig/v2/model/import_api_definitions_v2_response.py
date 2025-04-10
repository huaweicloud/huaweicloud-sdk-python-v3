# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportApiDefinitionsV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'list[Success]',
        'failure': 'list[Failure]',
        'swagger': 'Swagger',
        'group_id': 'str',
        'ignore': 'list[Ignore]'
    }

    attribute_map = {
        'success': 'success',
        'failure': 'failure',
        'swagger': 'swagger',
        'group_id': 'group_id',
        'ignore': 'ignore'
    }

    def __init__(self, success=None, failure=None, swagger=None, group_id=None, ignore=None):
        r"""ImportApiDefinitionsV2Response

        The model defined in huaweicloud sdk

        :param success: 导入成功信息
        :type success: list[:class:`huaweicloudsdkapig.v2.Success`]
        :param failure: 导入失败信息
        :type failure: list[:class:`huaweicloudsdkapig.v2.Failure`]
        :param swagger: 
        :type swagger: :class:`huaweicloudsdkapig.v2.Swagger`
        :param group_id: API分组编号
        :type group_id: str
        :param ignore: 被忽略导入的API信息
        :type ignore: list[:class:`huaweicloudsdkapig.v2.Ignore`]
        """
        
        super(ImportApiDefinitionsV2Response, self).__init__()

        self._success = None
        self._failure = None
        self._swagger = None
        self._group_id = None
        self._ignore = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if failure is not None:
            self.failure = failure
        if swagger is not None:
            self.swagger = swagger
        if group_id is not None:
            self.group_id = group_id
        if ignore is not None:
            self.ignore = ignore

    @property
    def success(self):
        r"""Gets the success of this ImportApiDefinitionsV2Response.

        导入成功信息

        :return: The success of this ImportApiDefinitionsV2Response.
        :rtype: list[:class:`huaweicloudsdkapig.v2.Success`]
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ImportApiDefinitionsV2Response.

        导入成功信息

        :param success: The success of this ImportApiDefinitionsV2Response.
        :type success: list[:class:`huaweicloudsdkapig.v2.Success`]
        """
        self._success = success

    @property
    def failure(self):
        r"""Gets the failure of this ImportApiDefinitionsV2Response.

        导入失败信息

        :return: The failure of this ImportApiDefinitionsV2Response.
        :rtype: list[:class:`huaweicloudsdkapig.v2.Failure`]
        """
        return self._failure

    @failure.setter
    def failure(self, failure):
        r"""Sets the failure of this ImportApiDefinitionsV2Response.

        导入失败信息

        :param failure: The failure of this ImportApiDefinitionsV2Response.
        :type failure: list[:class:`huaweicloudsdkapig.v2.Failure`]
        """
        self._failure = failure

    @property
    def swagger(self):
        r"""Gets the swagger of this ImportApiDefinitionsV2Response.

        :return: The swagger of this ImportApiDefinitionsV2Response.
        :rtype: :class:`huaweicloudsdkapig.v2.Swagger`
        """
        return self._swagger

    @swagger.setter
    def swagger(self, swagger):
        r"""Sets the swagger of this ImportApiDefinitionsV2Response.

        :param swagger: The swagger of this ImportApiDefinitionsV2Response.
        :type swagger: :class:`huaweicloudsdkapig.v2.Swagger`
        """
        self._swagger = swagger

    @property
    def group_id(self):
        r"""Gets the group_id of this ImportApiDefinitionsV2Response.

        API分组编号

        :return: The group_id of this ImportApiDefinitionsV2Response.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ImportApiDefinitionsV2Response.

        API分组编号

        :param group_id: The group_id of this ImportApiDefinitionsV2Response.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def ignore(self):
        r"""Gets the ignore of this ImportApiDefinitionsV2Response.

        被忽略导入的API信息

        :return: The ignore of this ImportApiDefinitionsV2Response.
        :rtype: list[:class:`huaweicloudsdkapig.v2.Ignore`]
        """
        return self._ignore

    @ignore.setter
    def ignore(self, ignore):
        r"""Sets the ignore of this ImportApiDefinitionsV2Response.

        被忽略导入的API信息

        :param ignore: The ignore of this ImportApiDefinitionsV2Response.
        :type ignore: list[:class:`huaweicloudsdkapig.v2.Ignore`]
        """
        self._ignore = ignore

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
        if not isinstance(other, ImportApiDefinitionsV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
