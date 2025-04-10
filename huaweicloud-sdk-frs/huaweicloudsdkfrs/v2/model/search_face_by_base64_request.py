# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchFaceByBase64Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'face_set_name': 'str',
        'enterprise_project_id': 'str',
        'body': 'FaceSearchBase64Req'
    }

    attribute_map = {
        'face_set_name': 'face_set_name',
        'enterprise_project_id': 'Enterprise-Project-Id',
        'body': 'body'
    }

    def __init__(self, face_set_name=None, enterprise_project_id=None, body=None):
        r"""SearchFaceByBase64Request

        The model defined in huaweicloud sdk

        :param face_set_name: 人脸库名称。
        :type face_set_name: str
        :param enterprise_project_id: 企业项目ID。FRS支持通过企业项目管理（EPS）对不同用户组和用户的资源使用，进行分账。当前仅支持按需计费模式。  获取方法：进入“[企业项目管理](https://console.huaweicloud.com/eps/?region&#x3D;cn-north-4#/projects/list)”页面，单击企业项目名称，在企业项目详情页获取Enterprise-Project-Id（企业项目ID）。  企业项目创建步骤请参见用户指南。 &gt; 说明： 创建企业项目后，在传参时，有以下三类场景。 - 携带正确的ID，正常使用FRS服务，账单的企业项目会被分类到企业ID对应的企业项目中。 - 携带格式正确但不存在的ID，正常使用FRS服务，账单的企业项目会显示对应不存在的企业项目ID。 - 不携带ID或格式错误ID（包含特殊字符等），正常使用FRS服务，账单的企业项目会被分类到\&quot;default\&quot;中。
        :type enterprise_project_id: str
        :param body: Body of the SearchFaceByBase64Request
        :type body: :class:`huaweicloudsdkfrs.v2.FaceSearchBase64Req`
        """
        
        

        self._face_set_name = None
        self._enterprise_project_id = None
        self._body = None
        self.discriminator = None

        self.face_set_name = face_set_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if body is not None:
            self.body = body

    @property
    def face_set_name(self):
        r"""Gets the face_set_name of this SearchFaceByBase64Request.

        人脸库名称。

        :return: The face_set_name of this SearchFaceByBase64Request.
        :rtype: str
        """
        return self._face_set_name

    @face_set_name.setter
    def face_set_name(self, face_set_name):
        r"""Sets the face_set_name of this SearchFaceByBase64Request.

        人脸库名称。

        :param face_set_name: The face_set_name of this SearchFaceByBase64Request.
        :type face_set_name: str
        """
        self._face_set_name = face_set_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this SearchFaceByBase64Request.

        企业项目ID。FRS支持通过企业项目管理（EPS）对不同用户组和用户的资源使用，进行分账。当前仅支持按需计费模式。  获取方法：进入“[企业项目管理](https://console.huaweicloud.com/eps/?region=cn-north-4#/projects/list)”页面，单击企业项目名称，在企业项目详情页获取Enterprise-Project-Id（企业项目ID）。  企业项目创建步骤请参见用户指南。 > 说明： 创建企业项目后，在传参时，有以下三类场景。 - 携带正确的ID，正常使用FRS服务，账单的企业项目会被分类到企业ID对应的企业项目中。 - 携带格式正确但不存在的ID，正常使用FRS服务，账单的企业项目会显示对应不存在的企业项目ID。 - 不携带ID或格式错误ID（包含特殊字符等），正常使用FRS服务，账单的企业项目会被分类到\"default\"中。

        :return: The enterprise_project_id of this SearchFaceByBase64Request.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this SearchFaceByBase64Request.

        企业项目ID。FRS支持通过企业项目管理（EPS）对不同用户组和用户的资源使用，进行分账。当前仅支持按需计费模式。  获取方法：进入“[企业项目管理](https://console.huaweicloud.com/eps/?region=cn-north-4#/projects/list)”页面，单击企业项目名称，在企业项目详情页获取Enterprise-Project-Id（企业项目ID）。  企业项目创建步骤请参见用户指南。 > 说明： 创建企业项目后，在传参时，有以下三类场景。 - 携带正确的ID，正常使用FRS服务，账单的企业项目会被分类到企业ID对应的企业项目中。 - 携带格式正确但不存在的ID，正常使用FRS服务，账单的企业项目会显示对应不存在的企业项目ID。 - 不携带ID或格式错误ID（包含特殊字符等），正常使用FRS服务，账单的企业项目会被分类到\"default\"中。

        :param enterprise_project_id: The enterprise_project_id of this SearchFaceByBase64Request.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def body(self):
        r"""Gets the body of this SearchFaceByBase64Request.

        :return: The body of this SearchFaceByBase64Request.
        :rtype: :class:`huaweicloudsdkfrs.v2.FaceSearchBase64Req`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this SearchFaceByBase64Request.

        :param body: The body of this SearchFaceByBase64Request.
        :type body: :class:`huaweicloudsdkfrs.v2.FaceSearchBase64Req`
        """
        self._body = body

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
        if not isinstance(other, SearchFaceByBase64Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
