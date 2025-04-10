# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSynthesisJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_info': 'DrugJobDto',
        'smiles': 'str',
        'params': 'SynthesisParamDto'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'smiles': 'smiles',
        'params': 'params'
    }

    def __init__(self, basic_info=None, smiles=None, params=None):
        r"""ShowSynthesisJobResponse

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        :param smiles: 分子SMILES表达式
        :type smiles: str
        :param params: 
        :type params: :class:`huaweicloudsdkeihealth.v1.SynthesisParamDto`
        """
        
        super(ShowSynthesisJobResponse, self).__init__()

        self._basic_info = None
        self._smiles = None
        self._params = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if smiles is not None:
            self.smiles = smiles
        if params is not None:
            self.params = params

    @property
    def basic_info(self):
        r"""Gets the basic_info of this ShowSynthesisJobResponse.

        :return: The basic_info of this ShowSynthesisJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        r"""Sets the basic_info of this ShowSynthesisJobResponse.

        :param basic_info: The basic_info of this ShowSynthesisJobResponse.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        self._basic_info = basic_info

    @property
    def smiles(self):
        r"""Gets the smiles of this ShowSynthesisJobResponse.

        分子SMILES表达式

        :return: The smiles of this ShowSynthesisJobResponse.
        :rtype: str
        """
        return self._smiles

    @smiles.setter
    def smiles(self, smiles):
        r"""Sets the smiles of this ShowSynthesisJobResponse.

        分子SMILES表达式

        :param smiles: The smiles of this ShowSynthesisJobResponse.
        :type smiles: str
        """
        self._smiles = smiles

    @property
    def params(self):
        r"""Gets the params of this ShowSynthesisJobResponse.

        :return: The params of this ShowSynthesisJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.SynthesisParamDto`
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this ShowSynthesisJobResponse.

        :param params: The params of this ShowSynthesisJobResponse.
        :type params: :class:`huaweicloudsdkeihealth.v1.SynthesisParamDto`
        """
        self._params = params

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
        if not isinstance(other, ShowSynthesisJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
